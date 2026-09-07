"""FANTECH"""

n = int(input())
f = input()
s = input()

count = 0

for i in range(n):
    if int(f[i]) + int(s[i]) != 9:
        count += 1

if not count:
    print("YES")
else:
    print("NO", count)
