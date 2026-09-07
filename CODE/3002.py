"""SOMCHAIJAIDEEEEEE"""

User = input()
Last = input()
AGE = str(input())

if len(User) >= 5 and len(Last)>= 5:
    pw = User[:2]+Last[-1]+(str(AGE))[-1]
else:
    pw = User[:1]+AGE+Last[-1]
print(pw)
