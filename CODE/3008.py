"""HEROINEalex"""
import math as m

a = float(input())
b = float(input())
c = float(input())

s = (a+b+c)/2
A = m.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"{A:.3f}")
