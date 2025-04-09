from datetime import datetime

class Folder:
    """
    Модель "Папка".
    user_id -- пользователь, которому принадлежит папка
    name -- название папки
    created_at -- дата создания
    """
    def __init__(self, folder_id: int, user_id: int, name: str, created_at: datetime):
        self.folder_id = folder_id
        self.user_id = user_id
        self.name = name
        self.created_at = created_at

    def dict(self) -> dict:
        return {
            "folder_id": self.folder_id,
            "user_id": self.user_id,
            "name": self.name,
            "created_at": self.created_at.isoformat()
        }
