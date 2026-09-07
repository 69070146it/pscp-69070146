"""KANAN"""

kon = int(input())
kk = int(input())
count = 1

for _ in range(kon - 1):
    kon = int(input())
    if kon > kk:
        kk = kon
        count = 1
    elif kon == kk:
        count += 1

print(kk)
print(count)
