"""lekkkoo"""

n = int(input())
maxe = 0

for i in range(n):
    num = int(input())
    if num%3 == 0 and num < maxe:
        maxe += 1
print(maxe)