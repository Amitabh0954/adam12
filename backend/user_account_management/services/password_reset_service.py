import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User
from backend.user_account_management.models.password_reset_token import PasswordResetToken
from backend.user_account_management.services.password_service import PasswordService
from backend.user_account_management.services.email_service import EmailService

class PasswordResetService:
    def __init__(self, session: Session, email_service: EmailService):
        self.session = session
        self.email_service = email_service
        self.password_service = PasswordService()

    def generate_reset_token(self, email: str) -> None:
        user = self.session.query(User).filter_by(email=email).first()
        if not user:
            return

        token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + timedelta(hours=24)
        reset_token = PasswordResetToken(user_id=user.id, token=token, expires_at=expires_at)
        self.session.add(reset_token)
        self.session.commit()

        reset_link = f"http://yourdomain.com/reset-password?token={token}"
        email_body = f"Click the link to reset your password: {reset_link}"
        self.email_service.send_email(user.email, "Password Reset", email_body)

    def reset_password(self, token: str, new_password: str) -> None:
        reset_token = self.session.query(PasswordResetToken).filter_by(token=token).first()
        if not reset_token or not reset_token.is_valid():
            raise ValueError("Invalid or expired reset token")

        user = self.session.query(User).get(reset_token.user_id)
        hashed_password = self.password_service.hash_password(new_password)
        user.hashed_password = hashed_password

        self.session.commit()
        self.session.delete(reset_token)
        self.session.commit()

#### 4. Implement controller to expose API for requesting password reset and resetting password

##### PasswordResetController