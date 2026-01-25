from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LoginAttempt(Base):
    __tablename__ = 'login_attempts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    attempt_time = Column(DateTime, default=datetime.utcnow)

#### 2. Implement authentication logic, including hashing and validation of passwords

Already implemented in `password_service.py`.

#### 3. Implement a service to handle login attempts and manage sessions

##### AuthService