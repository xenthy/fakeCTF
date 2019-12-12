import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def main(inf):
    """
    Read the `list.txt` file in order (top to bottom)

        For each valid IC, call `inf.set_infinity(True)`
        For each invalid IC, call `inf.set_infinity(False)`

        You should call inf.set_infinity() 1000 times
    """



class Infinity:
    infinity = ""
    def __init__(self, infinity):
        self.infinity = infinity
    def set_infinity(self, addon):
        self.infinity += "1" if addon else "0"
    def get_infinity(self):
        return self.infinity

def decrypt(inf):
    password_provided = inf.get_infinity()
    password = password_provided.encode()
    salt = b'~\xe1~_\\\x15_\xa8\x1f\xef-uI\x85\xdbS'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    encrypted = ""

    with open("encrypted.txt", "rb") as file:
        encrypted = file.read()

    f = Fernet(key)
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Input:\n{}\nYour input is wrong.".format(inf.get_infinity()))
        exit()
    print(decrypted.decode("utf-8"))

if __name__ == "__main__":
    infinity = Infinity("")
    main(infinity)
    decrypt(infinity)
    