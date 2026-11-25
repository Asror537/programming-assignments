goal = 100000
budget = 0
deposit = 0
day = 0

while budget < goal:
    deposit = int(input())
    while deposit < 0:
        deposit = int(input("No stealing from the piggy!\n"))
    budget += deposit
    day += 1

print(f"Goal reached in {day} days")