from genericpath import isfile
from pathlib import Path
from rich.prompt import Confirm
from time import sleep
import signal
from sys import exit

signal.signal(signal.SIGINT, lambda sig, frame: print("\nExiting the program. Goodbye!") or exit(0))

from cs.module import clear, encrypt_file, decrypt_file
from py_src.choice import ask_for_file_or_folder, ask_encryption_or_decryption, ask_for_multiprocessing, ask_for_password, ask_for_salt, ask_file_or_folder_file_path
from py_src.transform_folder import transform_folder

PASSWORD: str = ask_for_password()
SALT: str = ask_for_salt()
encrypting: bool = None
is_file: bool = None
multiprocessing: bool = ask_for_multiprocessing()

def main():
    while True:
        global encrypting, is_file
        encrypting = ask_encryption_or_decryption(encrypting)
        used_path = ask_file_or_folder_file_path()
        is_file = ask_for_file_or_folder(is_file)
        if encrypting:
            if is_file:
                encrypt_file(used_path, PASSWORD, SALT)
            elif not is_file:
                transform_folder(used_path, PASSWORD, SALT, encrypting, multiprocessing)
        elif not encrypting: # Decrypting
            if is_file:
                decrypt_file(used_path, PASSWORD, SALT)
            elif not is_file:
                transform_folder(used_path, PASSWORD, SALT, encrypting, multiprocessing)
        continue_choice = Confirm.ask("Do you want to continue?", default=True)
        if not continue_choice:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Continuing the program...")
            sleep(0.5)
            clear()

if __name__ == "__main__":
    main()