"""Scoresgame"""

base = int(input())
bonus = int(input())
day = int(input())

result1 = base + bonus

if day > 3:
    result1 = (base + bonus) * 1.5

print(result1)

if result1 >= 1500:
    aundub = 5
elif result1 >= 1000:
    aundub = 4
elif result1 >= 500:
    aundub = 3
elif result1 >= 200:
    aundub = 2
else:
    aundub = 1

print(aundub)

if aundub == 5 and day >= 7:
    print(99)
elif aundub == 4 and bonus > 300:
    print(88)
else:
    print(0)
