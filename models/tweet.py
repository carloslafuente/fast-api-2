# Python
from datetime import datetime
from typing import Optional
from uuid import UUID
# Pydantic
from pydantic import BaseModel
from pydantic import Field
# Models
from models.user import User


class Tweet(BaseModel):
    id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    creation_date: datetime = Field(default=datetime.now())
    update_date: Optional[datetime] = Field(default=None)
    user: User = Field(...)
