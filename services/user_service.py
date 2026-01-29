from sqlalchemy.orm import Session
from models.user import User

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValueError('Email and password are required')

        user = User(email=email)
        user.set_password(password)
        self.session.add(user)
        self.session.commit()
        return user