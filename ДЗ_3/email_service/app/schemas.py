from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EmailCreate(BaseModel):
    """
    Схема тела запроса при создании письма.
    """
    from_user_id: int = Field(..., examples=[1])
    to_user_id: int = Field(..., examples=[2])
    subject: str = Field(..., examples=["Hello"])
    body: str = Field(..., examples=["How are you?"])
    attachments: Optional[List[str]] = Field(default=None)


class EmailRead(BaseModel):
    """
    Схема ответа при получении письма.
    """
    message_id: int
    from_user_id: int
    to_user_id: int
    subject: str
    body: str
    created_at: datetime
    is_read: bool
    attachments: List[str] = []

    class Config:
        from_attributes = True

class EmailUpdate(BaseModel):
    """
    Схема для обновления (отметить письмо как прочитанное).
    """
    is_read: Optional[bool] = Field(default=None, example=True)
