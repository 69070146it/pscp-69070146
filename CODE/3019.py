"""SAFELOCK"""""
AUSKORN = "H"
LEK = "4567"

a = input()
b = input()

if a == AUSKORN and b == LEK:
    print("safe unlocked")
elif a == AUSKORN and b != LEK:
    print("safe locked - change digit")
elif a != AUSKORN and b == LEK:
    print("safe locked - change char")
else:
    print("safe locked")
