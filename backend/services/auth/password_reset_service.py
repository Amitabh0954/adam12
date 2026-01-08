import secrets
from datetime import datetime, timedelta
from backend.models.users.password_reset import PasswordResetRequest, PasswordResetConfirm
from backend.repositories.users.user_repository import UserRepository

user_repository = UserRepository()
reset_tokens = {}

def request_password_reset(request: PasswordResetRequest):
    user = user_repository.get_by_email(request.email)
    if not user:
        raise ValueError("Email not found")
    
    token = secrets.token_urlsafe()
    reset_tokens[request.email] = {
        'token': token,
        'expires_at': datetime.utcnow() + timedelta(hours=24)
    }

    # Implement sending email code here
    print(f"Password reset link: /reset/{token}")

def confirm_password_reset(confirm: PasswordResetConfirm):
    reset_info = reset_tokens.get(confirm.email)
    if not reset_info or reset_info['token'] != confirm.token or reset_info['expires_at'] < datetime.utcnow():
        raise ValueError("Invalid or expired token")
    
    user = user_repository.get_by_email(confirm.email)
    user.password = confirm.new_password
    user_repository.save(user)