from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    user_name: str
    email: str