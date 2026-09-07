"""BORIKARN"""

pay = int(input())

vats = pay*0.10

if vats < 50:
    vats = 50
elif vats > 1000:
    vats = 1000

ruam = pay+vats
ruam = ruam + (ruam*0.07)

print(f"{ruam:.2f}")
