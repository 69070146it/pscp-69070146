"""SUVARNNABUM"""
import math

START = float(input())
END = float(input())

H1 = int(START)
M1 = round((START - H1) * 100)

H2 = int(END)
M2 = round((END - H2) * 100)

VALID_START = 0 <= H1 <= 23 and 0 <= M1 <= 59
VALID_END = 0 <= H2 <= 23 and 0 <= M2 <= 59

if not VALID_START or not VALID_END:
    print("ERROR")
else:
    START = H1 * 60 + M1
    END = H2 * 60 + M2
    TIME = END - START

    if TIME < 0:
        print("ERROR")
    elif TIME <= 15:
        print("FREE")
    else:
        HOUR = math.ceil(TIME / 60)

        if HOUR == 1:
            print(25)
        elif HOUR == 2:
            print(50)
        elif HOUR == 3:
            print(80)
        elif HOUR == 4:
            print(110)
        elif HOUR == 5:
            print(145)
        elif HOUR == 6:
            print(180)
        elif HOUR <= 24:
            print(250)
        else:
            print("ERROR")
