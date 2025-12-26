from repositories.auth.user_repository import UserRepository
from repositories.auth.session_repository import SessionRepository
from models.session import Session

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.session_repository = SessionRepository()

    def login(self, email: str, password: str):
        user = self.user_repository.find_by_email(email)
        if not user or user.password != password:
            self.handle_failed_login(email)
            return {"message": "Invalid username or password", "status": 401}
        
        session = self.session_repository.find_by_user_id(user.id)
        if not session:
            session = Session(user.id)
        
        if not session.login():
            return {"message": "Account is locked due to too many failed login attempts", "status": 403}
        
        self.session_repository.save(session)
        return {"message": "Login successful", "status": 200, "user": {"id": user.id, "email": user.email}}

    def handle_failed_login(self, email: str):
        user = self.user_repository.find_by_email(email)
        if user:
            session = self.session_repository.find_by_user_id(user.id)
            if not session:
                session = Session(user.id)
            session.failed_login()
            self.session_repository.save(session)

    def logout(self, user_id: int):
        session = self.session_repository.find_by_user_id(user_id)
        if not session:
            return {"message": "Session not found", "status": 404}
        session.logout()
        self.session_repository.save(session)
        return {"message": "Logout successful", "status": 200}