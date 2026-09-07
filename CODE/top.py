"""DDD"""

n = int(input())

x = ""
print("*"*n)
for i in range(1, n + 1):
    x = x + str(i)

    print("*" + x + "*")
print("*"*n)