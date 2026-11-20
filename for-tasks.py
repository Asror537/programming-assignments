# for i in range(1, 10):
#     print(i)

#####

# name = input()
# n = int(input())

# for i in range(n):
#     print(name)

#####

# for i in range(1, 50):
#     if i % 2 == 0:
#         print(i)

#####

# n = int(input())
# sum = 0
# for i in range(1, n):
#     sum += i

# print(sum)

# #####

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
# print("start") 

#####

# num = int(input())

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

#####

# arr = ["apple", "banana", "kiwi"]

# for i in range(len(arr)):
#     print(f"{i+1}. {arr[i]}")

#####

# factorial = int(input())
# sum = 1

# for i in range(factorial):
#     sum = sum * (i+1)
# print(sum)

#####

# num = int(input())
# i = 0
# sum = 0

# while 0 != num:
#     sum = sum + (num % 10)
#     num = num // 10
# print(sum)

#####

# word = input()
# arr = ['a', 'e', 'o', 'u', 'i']
# count = 0

# for i in arr:
#     if i in word:
#         count += 1

# print(count)

#####

# password = "python123"
# check_password = input()
# attempts = 1

# while check_password.lower() != password:
#     attempts += 1
#     check_password = input("Wrong password, try again: ").lower()

#     if check_password == password:
#         print("welcome")
#         break
    
#     if attempts >= 3:
#         print("Account locked")
#         break

#####

# i = None
# arr = []
# sum = 0
# max = 0

# while i != 0:
#     i = int(input())
#     arr.append(i)
#     sum += 1
#     if max < i:
#         max = i
# print(f"largest: {max}, {sum-1} in  total")

#####

# for i in range(1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, " FizzBuzz")
#     elif i % 3 == 0:
#         print(i, " Fizz")
#     elif i % 5 == 0:
#         print(i, " Buzz")

#####

# word = input()
# length = len(word)
# i = 0
# word2 = ""
# while length > 0:
#     word2 += word[length-1]
#     length -= 1

# if word == word2:
#     print("palindrom")
# else:
#     print("not palindrom")


#####

# n = int(input())

# for i in range(2, n + 1):
#     counters = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             counters += 1

#     if counters == 2:
#         print(i)

#####

fibonaci = int(input())
sum = 0
firstnum = 0
secondnum = 1

for i in range(fibonaci):
    print(firstnum)
    sum = firstnum + secondnum
    firstnum = secondnum
    secondnum = sum