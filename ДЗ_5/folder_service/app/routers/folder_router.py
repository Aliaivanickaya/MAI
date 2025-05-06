from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas import FolderCreate, FolderRead, FolderUpdate
from app.services.folder_service import FolderService
from app.repositories.folder_repository import FolderRepository
from app.auth import verify_token

router = APIRouter(prefix="/folders", tags=["folders"])

folder_service = FolderService(FolderRepository())


@router.post("", response_model=FolderRead, dependencies=[Depends(verify_token)])
def create_folder(payload: FolderCreate):
    """
    Создание новой папки.
    """
    folder = folder_service.create_folder(payload.user_id, payload.name)
    return folder.dict()


@router.get("", response_model=List[FolderRead], dependencies=[Depends(verify_token)])
def list_all_folders():
    """
    Получение списка всех папок.
    """
    folders = folder_service.list_folders()
    return [f.dict() for f in folders]


@router.get("/{folder_id}", response_model=FolderRead, dependencies=[Depends(verify_token)])
def get_folder_by_id(folder_id: int):
    """
    Получение папки по ID.
    """
    folder = folder_service.get_folder(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folder.dict()


@router.patch("/{folder_id}", response_model=FolderRead, dependencies=[Depends(verify_token)])
def update_folder(folder_id: int, payload: FolderUpdate):
    """
    Обновить папку (переименовать).
    """
    try:
        folder = folder_service.update_folder(folder_id, payload.name)
        return folder.dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{folder_id}", dependencies=[Depends(verify_token)])
def delete_folder(folder_id: int):
    """
    Удалить папку по ID.
    """
    success = folder_service.delete_folder(folder_id)
    if not success:
        raise HTTPException(status_code=404, detail="Folder not found")
    return {"detail": "Folder deleted"}
