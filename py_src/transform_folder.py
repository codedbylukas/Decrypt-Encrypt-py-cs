import multiprocessing
import os
from pathlib import Path
from cs.module import encrypt_file, decrypt_file

process_list: list = []


def get_all_files(directory: Path, file_paths: list) -> list:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def transform_folder(
    folder_path: Path,
    password: str,
    salt: str,
    encrypting: bool,
    use_multiprocessing: bool,
) -> None:
    file_paths = []
    file_paths = get_all_files(folder_path, file_paths)
    for file_path in file_paths:
        if not use_multiprocessing:
            if encrypting:
                encrypt_file(file_path, password, salt)
            else:
                decrypt_file(file_path, password, salt)
        elif use_multiprocessing:
            if encrypting:
                process = multiprocessing.Process(
                    target=encrypt_file, args=(file_path, password, salt)
                )
                process.start()
                process_list.append(process)
            else:
                process = multiprocessing.Process(
                    target=decrypt_file, args=(file_path, password, salt)
                )
                process.start()
                process_list.append(process)
    if use_multiprocessing:
        for process in process_list:
            process.join()
        process_list.clear()
