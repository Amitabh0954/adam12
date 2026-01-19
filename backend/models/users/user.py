from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    password_hash: str
    status: str = field(default="active")  # Possible values: 'active', 'inactive', 'banned'
    role: str = field(default="user")  # Possible values: 'user', 'admin', 'moderator', etc.
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None