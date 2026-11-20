# n = int(input())
# if n == 0:
#     print("zero")
# elif n > 0:
#     print("positive")
# else:
#     print("negative")

# num = int(input())

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# s = int(input())

# if s >= 60:
#     print("pass")
# else:
#     print("fail")

# b = int(input())
# b1 = int(input())
# if b == b1:
#     print("equal")
# elif b > b1:
#     print(b)
# else:
#     print(b1)








# score = int(input("score: "))
# if score >= 90:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >= D and score < 70:
#     print("D")
# else:
#     print("F")

# year = int(input("enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#   print(f"{year} — leap year")
# else:
#   print(f"{year} — simple year")


# num = int(input("age: "))

# if num < 7:
#     print("free")
# elif num >= 7 and num <= 17:
#     print("10.000 som")
# elif num >= 18 and num <= 59:
#     print("20.000 som")
# else:
#     print("8000 som")

# f = int(input("first num: "))
# s = int(input("second num: "))
# mat = input("operator: ")

# if mat == "+":
#     print(f + s)
# elif mat == "-":
#     print(f - s)
# elif mat == "/":
#     print(f / s)
# elif mat == "*":
#     print(f * s)









price = 5000

# distance = int(input())
# time = int(input("time: "))
# rain = bool(input("1-yes, 2-no: "))

# if rain == True:
#     price = price + (price * 0.15)


# if time >= 22 or time <= 6:
#     price = price + (price * 0.25)


# if distance <= 2:
#     pass
# else:
#     price = price + ((distance / 2) * 2000)

# if price < 8000:
#     price = 8000

# print("price is: ", price)

###

# player1 = input()
# player2 = input()

# choice1 = input().lower()
# choice2 = input().lower()

# s = ["rock", "paper", "scissor"]

# if choice1 not in s or choice2 not in s:
#     print("write correct symbol")
#     choice1 = input("symbol: ")
#     choice1 = input("symbol: ")

# if choice1 == choice2:
#     print("It's a tie!")

# elif choice1 == "rock" and choice2 == "scissors":
#     print(player1, "wins!")

# elif choice1 == "scissors" and choice2 == "paper":
#     print(player1, "wins!")

# elif choice1 == "paper" and choice2 == "rock":
#     print(player1, "wins!")

# elif choice2 == "rock" and choice1 == "scissors":
#     print(player2, "wins!")

# elif choice2 == "scissors" and choice1 == "paper":
#     print(player2, "wins!")

# elif choice2 == "paper" and choice1 == "rock":
#     print(player2, "wins!")

# else:
#     print("Invalid input!")

###

# username = "qwerty"
# check_username = input("username: ")
# password = input("password: ")
# succes = True


# if check_username == "":
#     print("empty")
#     succes = False
# elif check_username != username:
#     print("wrong username")
#     succes = False

# if password == "":
#     print("empty")
#     succes = False
# elif password < 8:
#     print("password shorter than 8")
#     succes = False
# elif int in password:
#     print("no digit in password")
#     succes = False

# if succes == True:
#     print("Succes")
