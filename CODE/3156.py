"""CONAN"""

s = input()
k = int(input())

ABC = "abcdefghijklmnopqrstuvwxyz"
ans = ""

k = k % 26

for c in s:
    x = ABC.index(c)
    x = (x + k) % 26
    ans += ABC[x]

print(ans)
