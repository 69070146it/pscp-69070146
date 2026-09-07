"""schoolpj"""

school = input()

school = school.upper()

first = ord(school[0])
last = ord(school[-1])
length = len(school)

data = []

for i in range(10):
    if (i + 1) % 2 == 1:
        value = first + i
    else:
        value = last - i

    value = value % length

    if value > 9:
        value = value % 10

    data.append(value)

for i in range(2, 8):
    if i > 2:
        print(" ", end="")
    print(data[i], end="")
