from pathlib import Path
from rich.prompt import Confirm
import signal

signal.signal(signal.SIGINT, lambda sig, frame: print("\nExiting the program. Goodbye!") or exit(0))

from cs.module import encrypt_file, decrypt_file
from py_src.choice import ask_for_file_or_folder, ask_encryption_or_decryption, ask_for_password, ask_for_salt, ask_file_or_folder_file_path
from py_src.encrypt_folder import encrypt_folder

PASSWORD: str = ask_for_password()
SALT: str = ask_for_salt()
encrypting: bool = None
is_file: bool = None

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
                encrypt_folder(used_path, PASSWORD, SALT)
        elif not encrypting: # Decrypting
            if is_file:
                decrypt_file(used_path, PASSWORD, SALT)
            elif not is_file:
                print("Folder decryption is not yet implemented.")    
        continue_choice = Confirm.ask("Do you want to continue?", default=True)
        if not continue_choice:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Continuing the program...")

if __name__ == "__main__":
    main()