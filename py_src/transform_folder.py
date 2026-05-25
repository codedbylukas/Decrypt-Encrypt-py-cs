import os
from pathlib import Path
from cs.module import encrypt_file, decrypt_file

def get_all_files(directory: Path,  file_paths: list) -> list:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def transform_folder(folder_path: Path, password: str, salt: str, file: bool) -> None:
    file_paths = []
    file_paths = get_all_files(folder_path, file_paths)
    for file_path in file_paths:
        if file:
            encrypt_file(file_path, password, salt)
        elif not file:
            decrypt_file(file_path, password, salt)