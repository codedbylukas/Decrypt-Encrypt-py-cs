import os
import sys
from pythonnet import load

load("coreclr")
import clr

dll_path = os.path.abspath("DecryptFile.dll")
clr.AddReference(dll_path)

from SecureFileEncryptionNamespace import SecureFileEncryption

# 4. Funktionsaufruf testen
try:
    print("[*] Rufe C#-Verschlüsselung auf...")
    SecureFileEncryption.EncryptFileInPlace("a.txt", "dein_passwort", "dein_salt")
    print("[+] Erfolgreich ausgeführt.")
except Exception as e:
    print(f"[-] Fehler beim Ausführen der Methode: {e}")
