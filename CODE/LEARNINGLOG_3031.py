"""INK"""

import math

S, N = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    area = 3.1416 * (x * x + y * y)
    t = math.ceil(area / S)
    print(t)
