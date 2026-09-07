"""YEAR"""

n = int(input())

if n < 1582 and not n % 4:
    print("yes")
elif n >= 1582 and (not n % 400 or (not n % 4 and n % 100)):
    print("yes")
else:
    print("no")
