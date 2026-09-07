"""STATUSgasliquidwaeaser"""

temp = int(input())
unit = input()

if unit in ["F",'f']:
    temp = (temp - 32) * 5 / 9

if temp <= 0:
    print("solid")
elif temp >= 100:
    print("gas")
else:
    print("liquid")
