from typing import List, Optional
from datetime import datetime
from app.db import fake_folders_db, get_next_folder_id
from app.models import Folder


class FolderRepository:
    @staticmethod
    def create_folder(user_id: int, name: str) -> Folder:
        new_id = get_next_folder_id()
        folder = Folder(
            folder_id=new_id,
            user_id=user_id,
            name=name,
            created_at=datetime.utcnow()
        )
        fake_folders_db[new_id] = folder
        return folder

    @staticmethod
    def get_folder(folder_id: int) -> Optional[Folder]:
        return fake_folders_db.get(folder_id)

    @staticmethod
    def list_folders() -> List[Folder]:
        return list(fake_folders_db.values())

    @staticmethod
    def update_folder(folder: Folder):
        fake_folders_db[folder.folder_id] = folder

    @staticmethod
    def delete_folder(folder_id: int) -> bool:
        if folder_id in fake_folders_db:
            del fake_folders_db[folder_id]
            return True
        return False
