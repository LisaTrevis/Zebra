# print("Hello World")
#
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
#
# character_name = "Lisa"
# character_age = "42"
#
# print("There once was a woman named " + character_name + ".")
# print("She was " + character_age + " years old.")
#
# print("Zebra\n\"Academy\"")
#
# school = "Zebra\Academy"
# print(school)
#
# print(school.lower())
#
# print(school.upper())
#
# print(school.isupper())
#
# print(school.upper().isupper())
#
# print(len(school))
#
# print(school[6])
#
# print(school.index("a"))
#
# print(school.replace("Zebra", "Peacock"))
#
# # Numbers
# print(20)
#
# print(-230)
#
# print(3+4.5)
#
# print((3+4) * 2)
#
# print(10 % 3)
#
# my_num = 13
# print(str(my_num) + " is my fave number.")
#
# my_num = -5
# print(abs(my_num))
#
# # To set a number to a power
# print(pow(3, 2))
#
# print(max(3, 7))
# print(min(3, 7))
#
# print(round(3.2))
# print(round(3.7))
#
# # importing stuff
# from math import *
#
# print(floor(4.7))
# print(ceil(5.8))
# print(sqrt(49))
#
# # Getting input from a user
# # name = input("Enter your name: ")
# # age = input("Enter your age: ")
# # print("Hello, " + name + ". You are " + age + " years old.")
#
# # Calculator
# # num1 = input("Enter a number: ")
# # num2 = input("Enter another number: ")
# # result = float(num1) + float(num2)
# # print(result)
#
# # Grabbing data from lists
# friends = ["Sheila", "Katie", "Glenn", "Gabbe", "Miriam"]
# print(friends[2])
# print(friends[-3])
# print(friends[2:])
# print(friends[-3:])
# print(friends[1:3])
# friends[2] = "Kola"
# print(friends)
#
# # applying Python functions to lists
# more_friends = ["Elisabeth", "Nevdil", "Peter"]
#
# friends.extend(more_friends)
# print(friends)
#
# friends.append("Jen")
# print(friends)
#
# friends.insert(1, "Mom")
# print(friends)
#
# friends.remove("Jen")
# print(friends)
#
# friends.pop()
# print(friends)
#
# friends.sort()
# print(friends)
#
# friends.reverse()
# print(friends)
#
# friends2 = friends.copy()
# print(friends2)
#
# print(friends.index("Nevdil"))
#
# print(friends.count("Katie"))
#
# friends.clear()
# print(friends)

# Tuples: containers to store data that are immutable (can't be changed)
# Uses parens instead of square brackets like lists (arrays)
# Can access elements with square brackets just like a list (array)
# coordinates = (4, 7, 9)
# print(coordinates[2])

# Functions use the def keyword and require indentation. If there's 2 or more words,
# it's convention to use underscrores and lowercase
# nothing within the function after a return statement will not run:
# def sayhi(name):
#     print("Hello, " + name)
#
# sayhi("Lisa")
#
# def cube(num):
#     return num**3
#
# print(cube(2))

# is_female = True
# is_tall = True
#
# if is_female or is_tall:
#     print("You are either tall or a woman.")
#
# if is_female and is_tall:
#     print("You are a tall woman.")
# elif is_female and not(is_tall):
#     print("You are a short woman.")
# elif not(is_female) and is_tall:
#     print("You are a tall man.")
# else:
#     print("You are not a short man.")

# Comparison operators

# def max_num(num1, num2, num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(2,7,3))

# A better calculator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator!")

# Dictionaries allow us to store key value pairs

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# print(monthConversions["Nov"])
# print(monthConversions.get("Dec", "Not a valid key"))
# print(monthConversions.get("Luv", "Not a valid key"))

# While loops

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Guessing game

# secret_word = "pony"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You are out of guesses. You lose.")
# else:
#     print("You won!")

# For loop

# for letter in "Zebra Academy":
#     print(letter)

# friends = ["Sheila", "Jess", "Katie"]
# for name in friends:
#     print(name)

# for index in range(len(friends)):
#     print(friends[index])

# for index in range(10):
#     print(index)

# for index in range (3, 9):
#     print(index)

# for index in range(5):
#     if index == 0:
#         print("First item")
#     else:
#         print("Subsequent item")



