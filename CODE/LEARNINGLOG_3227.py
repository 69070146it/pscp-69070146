"""cards"""

card = input().upper()

a = {"A":"ace", "J":"jack", "Q":"queen", "K":"king"}
b = {"D":"diamonds", "H":"hearts", "S":"spades", "C":"clubs"}

x = card[:-1]
y = card[-1]

if x in a:
    x = a[x]

print(x, "of", b[y])
