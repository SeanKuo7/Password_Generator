# Author: Sean Bailey
# 210216
# linux$ pyinstaller ./pwgenerator.py -F --dist ./
# windows> pyinstaller .\pwgenerator.py --onefile --distpath .\

import string
import random
# from datetime import datetime
import time


class PasswordGenerator:
    def __init__(self) -> None:
        pass

    
    def run(self):
        while True:
            try:
                currentTime = int(time.time())
                random.seed(currentTime)
                inputStr = input(
                    'Input a number and a "?" (length = number & "?" add symbol:\n'
                )
                characters = string.ascii_letters + string.digits
                if inputStr == "":
                    inputStr = "32"
                if "?" in inputStr:
                    characters += string.punctuation
                    inputStr = inputStr[:-1]
                length = int(inputStr)
                password = "".join(random.choice(characters) for x in range(length))
                print("\n", password, "\n")
            except Exception as e:
                print("\nException:", e)


def main():
    try:
        generator = PasswordGenerator()
        generator.run()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
