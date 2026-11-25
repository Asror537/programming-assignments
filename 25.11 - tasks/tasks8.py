for i in range(8-1):
    for j in range(8-1):
        if (i + j) % 2 == 0:
            print("#", end=' ')
        else:
            print("-", end=' ')
    print("")