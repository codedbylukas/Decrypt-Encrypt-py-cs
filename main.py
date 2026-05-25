from cs.module import encrypt_file

PASSWORD = "dein_passwort"
SALT = "dein_salt"



if __name__ == "__main__":
    encrypt_file("a.txt", PASSWORD, SALT)
