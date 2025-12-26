from repositories.auth.auth_repository import AuthRepository
from models.session import Session
import hashlib

class AuthService:
    def __init__(self):
        self.auth_repository = AuthRepository()
        self.sessions = {}

    def login(self, data: dict):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {"message": "Email and password are required", "status": 400}

        user = self.auth_repository.find_by_email(email)
        if not user:
            return {"message": "Invalid email or password", "status": 401}

        encoded_password = hashlib.sha256(password.encode()).hexdigest()
        if user.password != encoded_password:
            return {"message": "Invalid email or password", "status": 401}

        session = Session(user_id=user.id)
        self.sessions[user.id] = session

        return {"message": "Login successful", "status": 200, "user": {"id": user.id, "email": user.email}}

    def invalidate_session(self, user_id: str):
        session = self.sessions.get(user_id)
        if session:
            session.invalidate()