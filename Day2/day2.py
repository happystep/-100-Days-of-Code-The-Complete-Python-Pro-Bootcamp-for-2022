#  Day2 - Beginner - Understanding Data Types and How to Manipulate Strings

# Data Types

# String

print("Hello"[0])

print("Hello"[4])

print("123" + "345")

# Integer

print(123 + 345)

print(123_456_789)

# Float

3.144159

# Boolean

True
False

num_char = len(input("What is your name?"))

print(type(num_char))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))

# Mathematical Operations in Python

3 + 5 
7 - 4
3 * 2
6 / 3
2 ** 2 

# PEMDAS

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Number Manipulation and F Strings in Python

print(round(8/3))

print(round(8/3 , 2))

print(round(8//3))

result = 4 / 2

result /= 2

print(result)

score = 0 

# User scores a poin

score += 1

print(score)

# f strings

score = 0
height = 1.8 
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")