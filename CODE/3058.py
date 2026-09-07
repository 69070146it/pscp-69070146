"""BRICCKBRIDGE"""

a = int(input())
b = int(input())
goal = int(input())

if goal//5 < b:
    big = goal//5
else:
    big = b

luea = goal - (big*5)

if luea <= a:
    print(luea)
else:
    print(-1)
