from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from backend.user_account_management.models.user import User
from backend.user_account_management.models.user_session import UserSession
from backend.user_account_management.models.login_attempt import LoginAttempt
from datetime import datetime, timedelta
import uuid

class AuthService:
    MAX_ATTEMPTS = 5
    TIME_FRAME = timedelta(minutes=15)
    SESSION_TIMEOUT = timedelta(minutes=20)

    def __init__(self, session: Session):
        self.session = session

    def login_user(self, email: str, password: str) -> UserSession:
        user = self.session.query(User).filter_by(email=email).first()
        if not user:
            self._log_attempt(None, False)
            raise ValueError("Invalid credentials")

        # Check recent unsuccessful attempts
        recent_attempts = self.session.query(LoginAttempt).filter_by(user_id=user.id).filter(
            LoginAttempt.attempt_time > datetime.utcnow() - self.TIME_FRAME,
            LoginAttempt.successful == 0
        ).count()

        if recent_attempts >= self.MAX_ATTEMPTS:
            raise ValueError("Max login attempts exceeded. Try again later.")

        if not check_password_hash(user.password, password):
            self._log_attempt(user.id, False)
            raise ValueError("Invalid credentials")

        self._log_attempt(user.id, True)
        return self._create_session(user.id)

    def _log_attempt(self, user_id: int, successful: bool) -> None:
        attempt = LoginAttempt(user_id=user_id, successful=successful)
        self.session.add(attempt)
        self.session.commit()

    def _create_session(self, user_id: int) -> UserSession:
        session_token = str(uuid.uuid4())
        user_session = UserSession(user_id=user_id, session_token=session_token)
        self.session.add(user_session)
        self.session.commit()
        return user_session

    def validate_session(self, session_token: str) -> bool:
        session = self.session.query(UserSession).filter_by(session_token=session_token).first()
        if not session:
            return False

        if datetime.utcnow() > session.last_activity + self.SESSION_TIMEOUT:
            self.session.delete(session)
            self.session.commit()
            return False

        session.last_activity = datetime.utcnow()
        self.session.commit()
        return True

#### 3. Implement a controller to expose the API for user login

##### AuthController