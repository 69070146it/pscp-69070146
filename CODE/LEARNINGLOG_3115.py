"""ARCADE OF TIME : STORE CHECK"""

num, _ = map(int, input().split())

diff = [0] * 1441

for _ in range(num):
    start, stop = map(int, input().split())
    diff[start] += 1
    diff[stop] -= 1

count = 0
open_shop = [0] * 1441

for i in range(1441):
    count += diff[i]
    open_shop[i] = count

times = list(map(int, input().split()))

ans = []

for t in times:
    ans.append(str(open_shop[t]))

print(" ".join(ans))
