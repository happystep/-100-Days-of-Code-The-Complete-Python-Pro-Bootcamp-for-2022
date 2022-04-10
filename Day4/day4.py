# Day 4 - Beginner - Randomisation and Python Lists

# Random integer
import random

random_integer = random.randint(1,10)
print(random_integer)

# import module

import my_module
print(my_module.pi)

# Random floating number
random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

# Python Lists

states_of_america = ["Delaware", "Pensylvania"]

print(states_of_america[0])

print(states_of_america[-2])

states_of_america.append("New Jersey")

print(states_of_america)

states_of_america.extend(["South Carolina","Virginia"])

print(states_of_america)

# lists of lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

