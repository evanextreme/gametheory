import time
import glob
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor
from os import path, getlogin, scandir
from string import ascii_uppercase

MAIN_DRIVE = 'C:'
WINDOWS_USERS_DIR = 'Users'

class Crypto():
    def __init__(self, public_exponent, key_size):
        self.num_threads = cpu_count()
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.home_directory = self._get_home_dir()
        self.private_key = rsa.generate_private_key(
            public_exponent=public_exponent,
            key_size=key_size,
            backend=default_backend()
        )

    def _get_home_dir(self):
        current_user = getlogin()
        home_dir = path.join(MAIN_DRIVE, WINDOWS_USERS_DIR, current_user)
        return home_dir

    def get_files(self):
        return glob.glob(path.join(self.home_directory, './**/'), recursive=True)


if __name__ == "__main__":
    user_crypt = Crypto(65537, 2048)
    print(user_crypt.get_files())
