from typing import Optional, List
from backend.models.users.session import Session

class SessionRepository:
    def __init__(self):
        self.sessions = []

    def create_session(self, session: Session) -> Session:
        self.sessions.append(session)
        return session

    def get_session_by_user_id(self, user_id: int) -> List[Session]:
        return [session for session in self.sessions if session.user_id == user_id]

    def delete_session(self, session: Session) -> None:
        self.sessions.remove(session)