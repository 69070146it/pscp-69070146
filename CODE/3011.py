"""COLORFORTUNE"""

a = input()
b = input()

if a == "Red" and b == "Yellow" or a == "Yellow" and b == "Red":
    print("Orange")
elif a == "Red" and b == "Blue" or a == "Blue" and b == "Red":
    print("Violet")
elif a == "Yellow" and b == "Blue" or a == "Blue" and b == "Yellow":
    print("Green")
elif a == b and (a in ["Red", "Yellow", "Blue"]):
    print(a)
else:
    print("Error")
