"""TEMP"""
T = float(input())
alp = input()
nuai = input()
a= 0
c= 0

if alp == "C":
    c = T
elif alp == "F":
    c = (T - 32) * 5 / 9
elif alp == "K":
    c = T - 273.15
elif alp == "R":
    c = (T - 491.67) * 5 / 9

if nuai == "C":
    a = c
elif nuai == "F":
    a = c * 9 / 5 + 32
elif nuai == "K":
    a = c + 273.15
elif nuai == "R":
    a = (c + 273.15) * 9 / 5

print(f"{a:.2f}")
