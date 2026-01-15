from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Session:
    id: int
    user_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)
    expires_at: datetime