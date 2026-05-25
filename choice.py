from rich.prompt import Prompt

def ask_for_file_or_folder(is_file: bool) -> bool:
    """" If its an file, return True, if its a folder, return False """
    choice = Prompt.ask("Do you want to encrypt a file or folder?", choices=["file", "folder"])
    if choice == "file":
        return True
    elif choice == "folder":
        return False
    else:
        print("Invalid choice. Please choose 'file' or 'folder'.")
        return ask_for_file_or_folder()


def ask_encryption_or_decryption(encrypting: bool) -> bool:
    """ Ask the user which encryption method they want to use. """
    choice = Prompt.ask("Which encryption method do you want to use?", choices=["encrypt", "enc", "decrypt", "dec"])
    if choice in ["encrypt", "enc"]:
        return True
    elif choice in ["decrypt", "dec"]:
        return False
    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
        return ask_encryption_or_decryption(encrypting)


def ask_for_password() -> str:
    """ Ask the user for a password. """
    password = Prompt.ask("Enter the password you want to use for encryption/decryption", password=True)
    return password

def ask_for_salt() -> str:
    """ Ask the user for a salt. """
    salt = Prompt.ask("Enter the salt you want to use for encryption/decryption")
    return salt
