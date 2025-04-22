from pydantic import BaseModel, Field
from datetime import datetime


class FolderCreate(BaseModel):
    """
    Схема для создания папки.
    """
    user_id: int = Field(..., examples=[1])
    name: str = Field(..., examples=["Inbox"])


class FolderRead(BaseModel):
    """
    Схема для ответа при получении папки.
    """
    folder_id: int
    user_id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class FolderUpdate(BaseModel):
    """
    Схема для обновления папки (переименовать).
    """
    name: str = Field(..., examples=["Archived"])
