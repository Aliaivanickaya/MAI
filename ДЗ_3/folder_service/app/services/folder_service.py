from typing import List, Optional
from app.models import Folder
from app.repositories.folder_repository import FolderRepository


class FolderService:
    def __init__(self, repo: FolderRepository):
        self.repo = repo

    def create_folder(self, user_id: int, name: str) -> Folder:
        return self.repo.create_folder(user_id, name)

    def get_folder(self, folder_id: int) -> Optional[Folder]:
        return self.repo.get_folder(folder_id)

    def list_folders(self) -> List[Folder]:
        return self.repo.list_folders()

    def update_folder(self, folder_id: int, new_name: str) -> Folder:
        folder = self.repo.get_folder(folder_id)
        if not folder:
            raise ValueError("Folder not found")
        folder.name = new_name
        self.repo.update_folder(folder)
        return folder

    def delete_folder(self, folder_id: int) -> bool:
        return self.repo.delete_folder(folder_id)
