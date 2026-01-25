from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from backend.user_account_management.models.password_reset_token import PasswordResetToken
from backend.user_account_management.models.user import User
from datetime import datetime, timedelta
import uuid
import smtplib
from email.mime.text import MIMEText

class PasswordResetService:
    TOKEN_EXPIRY = timedelta(hours=24)

    def __init__(self, session: Session):
        self.session = session

    def generate_reset_token(self, email: str) -> str:
        user = self.session.query(User).filter_by(email=email).first()
        if not user:
            raise ValueError("Email not found")

        token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + self.TOKEN_EXPIRY
        reset_token = PasswordResetToken(user_id=user.id, token=token, expires_at=expires_at)
        self.session.add(reset_token)
        self.session.commit()

        self._send_reset_email(user.email, token)
        return token

    def validate_reset_token(self, token: str) -> PasswordResetToken:
        reset_token = self.session.query(PasswordResetToken).filter_by(token=token).first()
        if not reset_token or reset_token.expires_at < datetime.utcnow():
            raise ValueError("Invalid or expired token")

        return reset_token

    def reset_password(self, token: str, new_password: str) -> None:
        reset_token = self.validate_reset_token(token)
        user = self.session.query(User).get(reset_token.user_id)
        if not user:
            raise ValueError("User not found")

        hashed_password = generate_password_hash(new_password)
        user.password = hashed_password
        self.session.commit()

        self.session.delete(reset_token)
        self.session.commit()

    def _send_reset_email(self, email: str, token: str) -> None:
        msg = MIMEText(f"To reset your password, use the following token: {token}")
        msg['Subject'] = 'Password Reset'
        msg['From'] = 'no-reply@yourapp.com'
        msg['To'] = email

        with smtplib.SMTP('localhost') as server:
            server.sendmail('no-reply@yourapp.com', [email], msg.as_string())

#### 3. Implement a controller to expose the API for password recovery

##### PasswordResetController