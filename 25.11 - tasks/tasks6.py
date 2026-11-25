import random

me = 0
pc = 0

mywin = 0
pcwin = 0

for i in range(1, 5):
    me = random.randint(1,6)
    pc = random.randint(1,6)

    if me > pc:
        print(f"You {me} - PC {pc}  You win")
        mywin += 1
    elif pc > me:
        print(f"You {me} - PC {pc}  PC win")
        PCwin += 1
    else:
        print("tie")

print("Final: you {me} - PC {pc}")
if me > pc:
    print("You are the champion")
elif pc > me:
    print("PC is the champion")
else:
    print("tie")