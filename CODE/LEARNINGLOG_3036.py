"""CASTLE"""

n = int(input())

row = 1
while n > row*row:
    row += 1

p = n - (row - 1)**2

if not p % 2:
    print(2*row - 3)
else:
    print(2*row - 2)
