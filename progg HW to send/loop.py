# n = int(input())
# for i in range(1, n+1):
#     print(i)

# arr = [5,4,3,4,5]
# sum = 0
# for i in arr:
#     sum = sum + i
# print(sum)

# nums = [2,6,5]
# maxnum = 0
# for i in nums:
#     if maxnum < i:
#         maxnum = i
# print("max - ", maxnum)






# i = 10
# while(i >= 1):
#     print(i)
#     i -= 1
# print("start")

# n = int(input())
# i = 0
# if n > 0:
#     while(i < n+1):
#         print(i)
#         i += 1
# else:
#     while i > n-1:
#         print(i)
#         i -= 1

# sum = 0
# i = 0
# while i <= 100:
#     sum += i
# print(sum)


# i = 0
# while(i < 20):
#     i += 2
#     print(i)

# p = int(input())
# while p != 0:
#     p = int(input("Write another number"))

# pin = 1234
# chekpin = int(input())
# while chekpin != pin:
#     chekpin = int(input("write the correct pin"))

# num = input()
# i = ""
# x = 0
# sum = 0
# while x < len(num):
#     i = int(num[x])
#     x += 1
#     sum += i    

# print(sum)

# budget = 0
# weeks = 0
# save = 250000
# price = 3000000
# while budget < price:
#     budget += save
#     weeks += 1

# print(weeks)

# budget = 1000000
# grow = 0.2
# double = budget * 2
# year = 0
# while budget <= double:
#     budget = budget + (budget * grow)
#     year += 1

# print(year)

# balance = 500000

# while True:
#     print("\n1 = balance")
#     print("2 = deposit")
#     print("3 = withdraw")
#     print("4 = exit")
    
#     choice = int(input("Choose an option: "))
    
#     if choice == 1:
#         print("Current balance:", balance, "so'm")
        
#     elif choice == 2:
#         amount = int(input("Enter deposit amount: "))
#         if amount > 0:
#             balance = balance + amount
#             print("Updated balance:", balance, "so'm")
#         else:
#             print("Amount must be greater than 0.")
            
#     elif choice == 3:
#         amount = int(input("Enter withdrawal amount: "))
#         if amount > balance:
#             print("Insufficient funds. You cannot withdraw more than your balance.")
#         elif amount <= 0:
#             print("Amount must be greater than 0.")
#         else:
#             balance = balance - amount
#             print("Updated balance:", balance, "so'm")
            
#     elif choice == 4:
#         print("Exiting ATM. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice. Please enter a number from 1 to 4.")

# n = int(input())
# temp = 0
# result = 0
# while n > 0:
#     temp = n % 10
#     result = (result * 10) + temp
#     n = n // 10
# print(result)