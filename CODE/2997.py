""""ELORATING"""

ra = int(input())
rb = int(input())
c = input()

ea = 1/(1+10**((rb-ra)/400))
eb = 1/(1+10**((ra-rb)/400))

if c == "A":
    print(f"{float(ea):.2f}")
elif c == "B":
    print(f"{float(eb):.2f}")
