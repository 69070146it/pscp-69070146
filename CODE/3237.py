""""TRIANGLE"""

n = int(input())

for i in range(1, n + 1):
    if i <= 1 or i == n:
        print("0" * i)
    elif n > 1:
        print("0" + "1" * (i - 2) + "0")
