import random

myhp = 20
dragonhp = 30

while myhp > 0 and dragonhp > 0:
    print(f"You {myhp} HP | Dragon {dragonhp} HP")
    mydamage = random.randint(3,8)
    dragondamage = random.randint(3,8)

    myhp -= dragondamage
    choose = input("a - attack, h - heal\n")
    
    if choose == "a":
        dragonhp -= mydamage
        print(f"You hit for {mydamage}\nDragon bites for {dragondamage}!")
    else:
        myhp += 5
        print(f"You heal {5} HP\nDragon bites for {dragondamage}!")

    

if myhp < dragonhp:
    print("You have been defeated!")
else:
    print("The dragon is defeated")    