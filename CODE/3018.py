"""OVERLAPPING"""

x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

le = max(x1, x2)
ri = min(x1 + w1, x2 + w2)
bot = max(y1, y2)
top = min(y1 + h1, y2 + h2)

if ri <= le or top <= bot:
    print("no overlapping")
else:
    print((ri - le)*(top - bot))
