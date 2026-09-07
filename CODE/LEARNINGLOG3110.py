"""UNICORN"""

d1 , d2 =  (input().upper()).split()
weight = float(input())

if d1 == "BKK" and d2 == "CNX":
    price = 10+(weight*30)
    print(f"{price:.2f}")
elif d1 == "CNX" and d2 == "UBP":
    price = 15+(weight*40)
    print(f"{price:.2f}")
elif d1 == "UBP" and d2 == "BKK":
    price = 20+(weight*40)
    print(f"{price:.2f}")
elif d1 == "BKK" and d2 == "PKT":
    price = 25+(weight*50)
    print(f"{price:.2f}")
elif d1 == "PKT" and d2 == "CNX":
    price = 30+(weight*60)
    print(f"{price:.2f}")
elif d1 == "UBP" and d2 == "PKT":
    price = 40+(weight*70)
    print(f"{price:.2f}")
else:
    print("Error")
