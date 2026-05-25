from cs.module import encrypt_file
from py_src.choice import ask_for_file_or_folder, ask_encryption_or_decryption, ask_for_password, ask_for_salt

PASSWORD = ask_for_password()
SALT = ask_for_salt()



if __name__ == "__main__":
    file_path = ask_for_file_or_folder()
    encrypting = ask_encryption_or_decryption(True)
    password = ask_for_password()
    salt = ask_for_salt()

    if encrypting:
        encrypt_file(file_path, password, salt)
