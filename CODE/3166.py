"""teacherchoices"""

ruam = 0
N = int(input())
passscores = True
_ = 0

for _ in range (N):
    scores = int(input())
    ruam += scores
    if scores < 50:
        passscores = False
print(f"{ruam/N:.1f}")

if ruam/N >= 60 and passscores:
    print("PASS")
else:
    print("FAIL")
