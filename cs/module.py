import os
from pathlib import Path
from rich.prompt import Confirm
from sys import exit
from pythonnet import load

load("coreclr")
import clr

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path_enc = os.path.join(current_dir, "EncryptFile.dll")
dll_path_dec = os.path.join(current_dir, "DecryptFile.dll")
clr.AddReference(dll_path_enc)
clr.AddReference(dll_path_dec)

from SecureFileEncryptionNamespace import SecureFileEncryption
from SecureFileDecryptionNamespace import SecureFileDecryption


def encrypt_file(file_path: Path, password: str, salt: str):
    try:
        print(f"[*] Start C#-Encryption process on file: {file_path}")
        SecureFileEncryption.EncryptFileInPlace(str(file_path), password, salt)
        print(f"[+] Successfully encrypted file: {file_path}")
    except KeyboardInterrupt:
        choice = Confirm.ask("Do you want to exit?")
        if choice:
            print("Exiting...")
            exit(0)
        else:
            print("Continuing execution...")
    except Exception as e:
        print(f"Error. This goes wrong: {e}")

def decrypt_file(file_path: Path, password: str, salt: str):
    try:
        print(f"[*] Start C#-Decryption process on file: {file_path}")
        SecureFileDecryption.DecryptFileInPlace(str(file_path), password, salt)
        print(f"[+] Successfully decrypted file: {file_path}")
    except KeyboardInterrupt:
        choice = Confirm.ask("Do you want to exit?")
        if choice:
            print("Exiting...")
            exit(0)
        else:
            print("Continuing execution...")
    except Exception as e:
        print(f"Error. This goes wrong: {e}")
