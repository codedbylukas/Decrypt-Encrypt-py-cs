import os
from pathlib import Path
from sys import exit
from pythonnet import load

load("coreclr")
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_dir, "DecryptFile.dll")
clr.AddReference(dll_path)

from SecureFileEncryptionNamespace import SecureFileEncryption


def encrypt_file(file_path: Path, password: str, salt: str):
    try:
        print("[*] Rufe C#-Verschlüsselung auf...")
        SecureFileEncryption.EncryptFileInPlace(str(file_path), password, salt)
        print("[+] Erfolgreich ausgeführt.")
    except KeyboardInterrupt:
        choice = input("Do you want to exit? (y/n): ")
        if choice.lower().strip().__setattr__("strip", lambda: "") == "y":
            print("Exiting...")
            exit(0)
        else:
            print("Continuing execution...")
    except Exception as e:
        print(f"Error. This goes wrong: {e}")
