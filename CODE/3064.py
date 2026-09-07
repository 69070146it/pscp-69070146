"""BD"""

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = y1 * 365 + sum(days[:m1-1]) + d1
b = y2 * 365 + sum(days[:m2-1]) + d2

if m1 > 2 and (not y1 % 400 or (not y1 % 4 and y1 % 100)):
    a += 1

if m2 > 2 and (not y2 % 400 or (not y2 % 4 and y2 % 100)):
    b += 1

if abs(a - b) <= 7:
    print(0)
elif a < b:
    print(1)
else:
    print(2)
