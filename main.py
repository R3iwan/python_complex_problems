# Problem 11: Prime Number Checker

import math

num1 = int(input("Enter a number to check it whether it's prime or not: "))


def prmNumb(num1):
    if num1 < 2:
        return False
    for i in range(2, int(math.sqrt(num1)) + 1):
        if num1 % i == 0:
            return False
    return True


if prmNumb(num1):
    print("It's prime number!")
else:
    print("It's not prime number!")

# Problem 12: Word Count!
""""
with open('file.pdf', 'r') as file:
    input = file.read()
words = input.split()
word_count = len(words)

print(f'The number of word count in file is {word_count}')
"""

# Problem 13: Password Generator
import random
import string

choice = int(input("Choose Which Password Generator option you need: \n1)Digits \n2)Special Characters \n3)With both Digits and Special Characters \n"))
pwdLen = int(input("Enter length of password: \n"))

match choice:
    case 1:
        char = string.digits
        pwd = ''.join(random.choice(char) for i in range(pwdLen))
        print("The generated password is:", pwd)
    case 2:
        char = string.punctuation
        pwd = ''.join(random.choice(char) for i in range(pwdLen))
        print("The generated password is:", pwd)
    case 3:
        char = string.digits + string.punctuation
        pwd = ''.join(random.choice(char) for i in range(pwdLen))
        print("The generated password is:", pwd)
    case 4:
        print("Invalid number")

# Problem 14: File Manipulation







