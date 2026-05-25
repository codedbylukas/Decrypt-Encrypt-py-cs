import os
from pathlib import Path
from rich.prompt import Confirm
from sys import exit
from pythonnet import load

load("coreclr")
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_dir, "EncpyptFile.dll")
clr.AddReference(dll_path)

from SecureFileEncryptionNamespace import SecureFileEncryption


def encrypt_file(file_path: Path, password: str, salt: str):
    try:
        print("[*] Rufe C#-Verschlüsselung auf...")
        SecureFileEncryption.EncryptFileInPlace(str(file_path), password, salt)
        print("[+] Erfolgreich ausgeführt.")
    except KeyboardInterrupt:
        choice = Confirm.ask("Do you want to exit?")
        if choice:
            print("Exiting...")
            exit(0)
        else:
            print("Continuing execution...")
    except Exception as e:
        print(f"Error. This goes wrong: {e}")
