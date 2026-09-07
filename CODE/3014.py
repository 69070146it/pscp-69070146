"""MILK"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

milk = d // a
cap = milk

if b:
    while cap >= b:
        exchange = cap // b
        milk += exchange * c
        cap = cap % b + exchange * c

print(milk)
