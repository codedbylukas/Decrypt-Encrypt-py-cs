from pathlib import Path
from rich.prompt import Prompt


def ask_for_file_or_folder(is_file: bool) -> bool:
    """ " If its an file, return True, if its a folder, return False"""
    choice = Prompt.ask(
        "Do you want to encrypt a file or folder?", choices=["file", "folder"]
    )
    if choice == "file":
        return True
    elif choice == "folder":
        return False
    else:
        print("Invalid choice. Please choose 'file' or 'folder'.")
        return ask_for_file_or_folder()


def ask_encryption_or_decryption(encrypting: bool) -> bool:
    """Ask the user which encryption method they want to use."""
    choice = Prompt.ask(
        "Which operation do you want to perform?",
        choices=["encrypt", "enc", "decrypt", "dec"],
    )
    if choice in ["encrypt", "enc"]:
        return True
    elif choice in ["decrypt", "dec"]:
        return False
    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
        return ask_encryption_or_decryption(encrypting)


def ask_file_or_folder_file_path() -> Path:
    used_path = Prompt.ask(
        "Enter the path to the file or folder you want to encrypt/decrypt"
    )
    path = Path(used_path)
    if not path.exists():
        print("The path you entered does not exist. Please enter a valid path.")
        return ask_file_or_folder_file_path()
    else:
        return used_path


def ask_for_multiprocessing() -> bool:
    """Ask the user if they want to use multiprocessing."""
    choice = Prompt.ask(
        "Do you want to use multiprocessing?",
        default="no",
        choices=["yes", "y", "no", "n"],
    )
    if choice == "yes" or choice == "y":
        return True
    elif choice == "no" or choice == "n":
        return False
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        return ask_for_multiprocessing()


def ask_for_password() -> str:
    """Ask the user for a password."""
    password = Prompt.ask(
        "Enter the password you want to use for encryption/decryption", password=True
    )
    return password


def ask_for_salt() -> str:
    """Ask the user for a salt."""
    salt: str = Prompt.ask("Enter the salt you want to use for encryption/decryption")
    return salt
