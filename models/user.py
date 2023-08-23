from pydantic import BaseModel
from typing import Optional

class UserBaseModel(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None

