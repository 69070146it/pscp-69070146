"""BBONUS"""

p, y, s = input().split()
y = int(y)
s = int(s)

if p == "M":
    E = 1500
    a, c, d = 0.06, 0.08, 0.10
elif p == "B":
    E = 1000
    a, c, d = 0.05, 0.06, 0.07
else:
    E = 500
    a, c, d = 0.04, 0.05, 0.06

if y <= 5:
    R = a
elif y <= 10:
    R = c
else:
    R = d

print(int(E + s * R))
