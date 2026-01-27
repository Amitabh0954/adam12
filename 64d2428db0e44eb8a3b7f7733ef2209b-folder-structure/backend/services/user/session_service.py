# Epic Title: User Account Management

from backend.models.user.session import Session
from backend.repositories.user.session_repository import SessionRepository
from backend.repositories.user.user_repository import UserRepository

class SessionService:
    def __init__(self, session_repository: SessionRepository, user_repository: UserRepository):
        self.session_repository = session_repository
        self.user_repository = user_repository
    
    def create_session(self, user_id: int) -> Session:
        new_session = Session(session_id="generated_session_id", user_id=user_id)  # Example ID management
        self.session_repository.add_session(new_session)
        return new_session
    
    def validate_session(self, session_id: str, timeout: int) -> bool:
        session = self.session_repository.get_session_by_id(session_id)
        if session and not session.is_expired(timeout):
            session.update_last_accessed()
            self.session_repository.add_session(session)  # Simulating update
            return True
        return False
    
    def invalidate_user_sessions(self, user_id: int):
        self.session_repository.invalidate_sessions(user_id)