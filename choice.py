from rich.prompt import Prompt

def ask_for_file_or_folder() -> bool:
    choice = Prompt.ask("Do you want to encrypt a file or folder?", choices=["file", "folder"])
    if choice == "file":
        return True
    elif choice == "folder":
        return False
    else:
        print("Invalid choice. Please choose 'file' or 'folder'.")
        return ask_for_file_or_folder()