from typing import Dict

from app.models import Folder

fake_folders_db: Dict[int, Folder] = {}

fake_folder_id_seq = 0


def get_next_folder_id() -> int:
    global fake_folder_id_seq
    fake_folder_id_seq += 1
    return fake_folder_id_seq
