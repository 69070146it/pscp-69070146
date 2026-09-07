"""DEK"""

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

a, day = input().split()
a = int(a)

if a < 5:
    PAY = 0
elif a <= 18:
    PAY = 100
else:
    PAY = 150

B = PAY // 2

if day == "Wed":
    print(B)
else:
    print(PAY)
