"""RAMENRABBIT"""

size, typ = input().split()

if size == "S":
    price = 60 if typ == "R" else 80
elif size == "M":
    price = 80 if typ == "R" else 100
else:
    price = 100 if typ == "R" else 120

topping = input().split()

if topping[0] == "P":
    price += 15 * int(topping[1])
elif topping[0] == "E":
    price += 10 * int(topping[1])

print(price)
