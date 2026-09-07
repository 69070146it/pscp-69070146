"""harn10"""

n = int(input())

for i in range(n-(n%10),-1,-10):
    print(i, end=" ")
