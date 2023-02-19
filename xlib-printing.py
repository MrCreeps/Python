import time
import msvcrt

def xprint(message):
    for character in message:
        print(character, end="")
        time.sleep(0.06)
    print(end="\n")

def xprint_nl(message): #no line
    for character in message:
        print(character, end="")
        time.sleep(0.06)

def xprint_we(message): #wait enter
    speed = 0.04
    for character in message:
        if msvcrt.kbhit() and (msvcrt.getch() == b' ' or msvcrt.getch() == b'space'):
            speed = 0.0004
        else:
            speed = 0.04
        print(character, end="")
        time.sleep(speed)
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b'\r':
            print("\r")
            break
