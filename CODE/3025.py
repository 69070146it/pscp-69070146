"""seasonw2e"""

month = int(input())
days = int(input())

if month <= 3:
    if month ==3 and days >= 21:
        print("spring")
    else:
        print("winter")

elif month <= 6:
    if month == 6 and days >= 21:
        print("summer")
    else:
        print("spring")

elif month <= 9:
    if month == 9 and days >= 21:
        print("fall")
    else:
        print("summer")

else:
    if month == 12 and days >= 21:
        print("winter")
    else:
        print("fall")
