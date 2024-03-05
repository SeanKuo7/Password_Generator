# Author: Sean Bailey
# 210216
# linux$ pyinstaller ./passwordGenerator.py -F --dist ./
# windows> pyinstaller .\src\passwordGenerator.py --onefile --distpath .\

import string
import random
from datetime import datetime
import secrets
import asyncio
from loadingAnimation import LoadingAnimation

class PasswordGenerator:
    characters = string.ascii_letters + string.digits
    charset = characters
    maxGeneratingInterval = 100
    defaultLen = "128"

    def __init__(self) -> None:
        pass

    def getRandomChar(self):
        # current_time = int(time.time())
        # current_time = int(datetime.now().timestamp())
        currentTimeWithMs = int(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        random.seed(currentTimeWithMs)
        return random.choice(self.charset)

    async def asyncioSleepMilliseconds(self, milliseconds):
        await asyncio.sleep(milliseconds / 1000)

    def sleepMilliseconds(self, milliseconds):
        asyncio.run(self.asyncioSleepMilliseconds(milliseconds))

    def getSecretChar(self):
        currentTimeWithMs = int(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        self.sleepMilliseconds(
            currentTimeWithMs % self.maxGeneratingInterval
        )  # extra randomness
        return secrets.choice(self.charset)

    def run(self):
        while True:
            try:
                animation = LoadingAnimation()
                inputStr = input(
                    """(number = length, default to 128, will include special characters if end with '?'. ^c to exit)\nInput a number and an optional '?': """
                )
                animation.start()
                self.charset = self.characters
                if inputStr == "":
                    inputStr = self.defaultLen
                if "?" in inputStr:
                    self.charset += string.punctuation
                    inputStr = inputStr[:-1]  # trim one char
                length = int(inputStr)
                randomString = "".join(self.getSecretChar() for x in range(length))
                animation.stop()
                print("\n", randomString, "\n")
            except Exception as e:
                print("An error occurred:", e, "\n")


def main():
    try:
        generator = PasswordGenerator()
        generator.run()
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
