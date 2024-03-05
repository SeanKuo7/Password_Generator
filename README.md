# Password_Generator

## requirement:
python3, pip, pyinstaller

## compile to binary

```shell

linux$ pyinstaller ./passwordGenerator.py -F --dist ./
windows> pyinstaller .\src\passwordGenerator.py --onefile --distpath .\
```

## False positive
Windows defender may block the compiled binary, execute action restore in the Windows defender.