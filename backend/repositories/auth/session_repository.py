from models.session import Session
from typing import Optional

class SessionRepository:
    def __init__(self):
        self.sessions = []

    def find_by_user_id(self, user_id: int) -> Optional[Session]:
        return next((session for session in self.sessions if session.user_id == user_id), None)

    def save(self, session: Session) -> None:
        existing_session = self.find_by_user_id(session.user_id)
        if existing_session:
            self.sessions = [session if s.user_id == session.user_id else s for s in self.sessions]
        else:
            self.sessions.append(session)