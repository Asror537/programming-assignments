word = input()
vowels = ['a', 'e', 'u', 'o', 'i']
countV = 0
countC = 0

for i in word:
    if i in vowels:
        countV += 1
    else:
        countC += 1

print(f"vowels {countV}, consonants {countC}")
if countC > countV:
    print("vowels win")
elif countV > countC:
    print("Vowels win")
else:
    print("tie")