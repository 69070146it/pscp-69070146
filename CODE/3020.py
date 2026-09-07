""""COKESS"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

cap = 0
money = 0

for _ in range(d):
    if b != 0 and cap >= b:
        money += c
        cap = cap - b + 1
    else:
        money += a
        cap += 1

print(money)
