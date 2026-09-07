"""PRIMESNUMBERfindndn"""

a, b = map(int, input().split())

prime = []

for n in range(a, b + 1):
    if n >= 2:
        check = True

        for i in range(2, n):
            if not n % i:
                check = False
                break

        if check:
            prime.append(n)

if prime:
    print(*prime)

print("Total primes:", len(prime))
