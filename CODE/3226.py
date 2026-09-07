"""FER"""

from decimal import Decimal, ROUND_DOWN, getcontext

n = input()
k = int(input())

getcontext().prec = len(n.replace(".", "")) + k + 20

n = Decimal(n)

for _ in range(k):
    increase = n * Decimal("0.0381")
    increase = increase.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
    n += increase

print(f"{n:.2f}")
