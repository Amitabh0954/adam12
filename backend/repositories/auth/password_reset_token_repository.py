from models.password_reset_token import PasswordResetToken
from typing import Optional

class PasswordResetTokenRepository:
    def __init__(self):
        self.tokens = []

    def save(self, token: PasswordResetToken) -> None:
        self.tokens.append(token)

    def find_by_token(self, token: str) -> Optional[PasswordResetToken]:
        return next((t for t in self.tokens if t.token == token), None)