"""taxical"""

km = int(input())

price = 35

if km >= 1:
    price += (min(km, 10) - 1) * 5

if km > 10:
    price += (km - 10) * 8

if not km:
    price = 0

print(price)
