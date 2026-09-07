""""BASIC ATM"""

n = int(input())

if n < 100:
    print("ERROR")
elif n > 20000:
    print("ERROR")
elif n % 100:
    print("ERROR")
else:
    for i in range(3):
        if not i:
            X = 1000
        elif i == 1:
            X = 500
        else:
            X = 100

        if n // X > 0:
            print(X, "=", n // X)

        n = n % X
