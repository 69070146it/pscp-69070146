"""cofeemate"""

ruam = 0
n = int(input())
prices = []

for _ in range(n):
    price = int(input())
    ruam += price
    prices.append(price)

print(ruam)
print(max(prices))
print(min(prices))
avg = ruam/n
print(f"{avg:.1f}")
