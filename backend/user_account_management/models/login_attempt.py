from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LoginAttempt(Base):
    __tablename__ = 'login_attempts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    attempt_time = Column(DateTime, default=datetime.utcnow)
    successful = Column(Integer, default=False)

#### 2. Implement services for user authentication and session management

##### AuthService