import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User
from backend.user_account_management.models.user_session import UserSession
from backend.user_account_management.models.login_attempt import LoginAttempt
from backend.user_account_management.services.password_service import PasswordService

class AuthService:
    MAX_FAILED_ATTEMPTS = 5
    SESSION_DURATION = timedelta(minutes=30)
    LOCKOUT_DURATION = timedelta(minutes=15)
    
    def __init__(self, session: Session):
        self.session = session
        self.password_service = PasswordService()

    def register_login_attempt(self, user: User) -> bool:
        now = datetime.utcnow()
        attempt = LoginAttempt(user_id=user.id, attempt_time=now)
        self.session.add(attempt)
        self.session.commit()

        # Check failed attempts in the lockout duration
        past_attempts = self.session.query(LoginAttempt).filter(
            LoginAttempt.user_id == user.id,
            LoginAttempt.attempt_time > now - self.LOCKOUT_DURATION
        ).count()

        return past_attempts < self.MAX_FAILED_ATTEMPTS

    def authenticate_user(self, email: str, password: str) -> str:
        user = self.session.query(User).filter_by(email=email).first()
        if not user:
            raise ValueError("Invalid email or password")

        # Check if user is locked out
        if not self.register_login_attempt(user):
            raise ValueError("Too many failed attempts, please try again later")

        if not self.password_service.check_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")

        session_token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + self.SESSION_DURATION
        user_session = UserSession(user_id=user.id, session_token=session_token, expires_at=expires_at)
        self.session.add(user_session)
        self.session.commit()

        return session_token

    def validate_session(self, session_token: str) -> bool:
        user_session = self.session.query(UserSession).filter_by(session_token=session_token).first()
        if not user_session or not user_session.is_active():
            return False
        return True

#### 4. Implement a controller to expose login and session management endpoints

##### AuthController