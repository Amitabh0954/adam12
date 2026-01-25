from models.user import User
from schemas.user import UserSchema
from sqlalchemy.orm import Session
from marshmallow import ValidationError

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, data: dict) -> User:
        try:
            user_data = UserSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

#### 4. Create `controllers/user_controller.py` for Flask endpoints