from models.password_reset import PasswordResetToken
from typing import Optional

class PasswordResetRepository:
    def __init__(self):
        self.tokens = []

    def save(self, token: PasswordResetToken) -> None:
        self.tokens.append(token)

    def find_by_token(self, token: str) -> Optional[PasswordResetToken]:
        return next((t for t in self.tokens if t.token == token), None)

    def invalidate_token(self, token: str) -> None:
        reset_token = self.find_by_token(token)
        if reset_token:
            reset_token.invalidate()