"""CHANOM"""

p, g = input().split()
g = float(g)


t, s, c = input().split()
s = int(s)
c = float(c)

pearl = {"H": 5, "O": 3, "J": 2}
tea = {
    "R": [12, 18, 25],
    "T": [15, 20, 30],
    "M": [10, 15, 20]
}

total = g * pearl[p] + tea[t][s - 1] * c

if total.is_integer():
    print(int(total))
else:
    print(total)
