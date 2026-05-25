from cs.module import encrypt_file
from py_src.choice import ask_for_file_or_folder, ask_encryption_or_decryption, ask_for_password, ask_for_salt, ask_file_or_folder_file_path

PASSWORD = ask_for_password()
SALT = ask_for_salt()
encrypting: bool = None
is_file: bool = None

if __name__ == "__main__":
    encrypting = ask_encryption_or_decryption(encrypting)
    used_path = ask_file_or_folder_file_path()
    is_file = ask_for_file_or_folder(is_file)
    if encrypting:
        encrypt_file(used_path, PASSWORD, SALT)
