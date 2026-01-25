from sqlalchemy.orm import Session
from backend.user_account_management.models.user import User
from backend.user_account_management.schemas.user_schema import UserSchema
from marshmallow import ValidationError

class ProfileService:
    def __init__(self, session: Session):
        self.session = session

    def update_profile(self, user_id: int, data: dict) -> User:
        user = self.session.query(User).get(user_id)
        if not user:
            raise ValueError("User not found")

        try:
            valid_data = UserSchema().load(data, partial=True)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        for key, value in valid_data.items():
            setattr(user, key, value)
        
        self.session.commit()
        return user

#### 3. Implement a controller to expose the API for profile updates

##### ProfileController