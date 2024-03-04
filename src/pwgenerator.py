# Author: Sean Bailey
# 210216
# linux$ pyinstaller ./pwgenerator.py -F --dist ./
# windows> pyinstaller .\pwgenerator.py --onefile --distpath .\

import string
import random
from datetime import datetime

while True:
    try:
        random.seed(datetime.now())
        inputStr = input(
            "Input a number and a \"?\" (length = number & \"?\" add symbol:\n"
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
    except:
        print("\nInvalid input\n")
