""""CALPLUS1"""

n = int(input())
digit = 0
for i in range(1, n + 1):
    digit += len(str(i))

if n == 1:
    print(digit)
else:
    print(digit + n)
