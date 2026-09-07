"""PONRUAMMAKKWA"""

n = int(input())
u = 0
z = ""

for i in range(n):
    c = int(input())
    e = int(input())

    if c > e:
        m = c
    else:
        m = e

    u += m
    z += str(m)

    if i < n - 1:
        z += " + "

if n == 1:
    print(z)
else:
    print(f"{z} = {u}")
