moves = ['rock', 'paper', 'scissor']

myscore = 0
pcscore = 0

for i in range(2):
    pc = random.choice(moves)
    you = input()
    
    myindex = moves.index(you)
    pcindex = moves.index(pc)

    if myindex == 2 and pcindex == 0:
        pcscore += 1
        print(f"You choose {you} - PC win!")
    elif pcindex == 2 and myindex == 0:
        myscore += 1
        print(f"PC choose {pc} - YOU win!")
    elif myindex > pcindex:
        myscore += 1
        print(f"PC choose {pc} - YOU win!")
    elif pcindex > myindex:
        pcscore += 1
        print(f"You choose {you} - PC win!")

if myscore > pcscore:
    print("YOU win")
elif pcscore > myscore:
    print("PC wins")
else:
    print("tie")