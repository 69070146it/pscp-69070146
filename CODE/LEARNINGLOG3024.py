"""SUR{ISE}"""

total = float(input())
highest = float(input())

for x in range(int(highest) + 1):
    y = total - highest - x

    if 0 <= y <= highest:
        if highest - min(x, y) > 2:
            print("Surprising")
            break
else:
    print("Not surprising")
