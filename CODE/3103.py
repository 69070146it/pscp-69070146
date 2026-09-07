"""countsara"""

n = int(input())
count = 0

for _ in range(n):
    ch = input().upper()
    for i in "AEIOU":
        if ch == i:
            count += 1
print(count)
