import random

number = random.randint(1,20)
usernum = int(input())
case = True

while case:
    if usernum != number:
        if usernum < number:
            print("too low!")
        elif usernum > number:
            print("too high!")
        usernum = int(input())
    else:
        print("You got it!")
        case = False