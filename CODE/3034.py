"""POD"""

n , k = map(int, input().split())

count = [0]*k

for _ in range(n):
    x = int(input())
    count[x-1] += 1

print(n-min(count)*k)
