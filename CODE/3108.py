"""rakapromo"""

a, b, c = map(int, input().split())

price = a * 25 + b * 40 + c * 55

if a + b + c >= 3:
    price = price * 90 // 100

print(price)
