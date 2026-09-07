"""aeiou"""

www = input().lower()

a = e = i = o = u = 0

for x in www:
    if x == "a":
        a += 1
    elif x == "e":
        e += 1
    elif x == "i":
        i += 1
    elif x == "o":
        o += 1
    elif x == "u":
        u += 1

if a:
    print("a :", a)
if e:
    print("e :", e)
if i:
    print("i :", i)
if o:
    print("o :", o)
if u:
    print("u :", u)
