# Author: Sean Bailey
# 210216
# linux$ pyinstaller ./pwgenerator.py -F --dist ./
# windows> pyinstaller .\pwgenerator.py --onefile --distpath .\

import string
import random
from datetime import datetime
import time
import secrets


class PasswordGenerator:
    characters = string.ascii_letters + string.digits
    charset = characters
    defaultLen = "32"
    
    def __init__(self) -> None:
        pass

    def getRandomChar(self):
        # current_time = int(time.time())
        # current_time = int(datetime.now().timestamp())
        currentTimeWithMs = int(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        random.seed(currentTimeWithMs)
        return random.choice(self.charset)
    
    def getSecretChar(self):
        return secrets.choice(self.charset)
    
    def run(self):
        while True:
            try:
                currentTime = int(time.time())
                random.seed(currentTime)
                inputStr = input(
                    'Input a number and a "?" (length = number & "?" add symbol:\n'
                )
                self.charset = self.characters
                if inputStr == "":
                    inputStr = self.defaultLen
                if "?" in inputStr:
                    self.charset += string.punctuation
                    inputStr = inputStr[:-1]
                length = int(inputStr)
                password = "".join(self.getSecretChar() for x in range(length))
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
