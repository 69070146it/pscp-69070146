""""sahakornrongleearn"""

from decimal import Decimal, ROUND_HALF_UP

m = input()
n = int(input())

total = Decimal("0")

for _ in range(n):
    total += Decimal(input())

if m == "Y":
    total *= Decimal("0.95")
elif total >= 500:
    total *= Decimal("0.97")

total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(total)
