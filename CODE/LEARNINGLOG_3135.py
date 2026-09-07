"""KONGKWANLAEKAMOY"""

N, K, T = map(int, input().split())

now = 1
count = 1

if T == 1:
    print(1)
else:
    while True:
        now = (now + K - 1) % N + 1

        if now == 1:
            break

        count += 1

        if now == T:
            break

    print(count)
