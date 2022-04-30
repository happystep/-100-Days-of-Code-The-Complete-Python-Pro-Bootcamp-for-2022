# Day 26 - Intermediate - List Comprehension and the NATO Alphabet (also dictionary comprehensions)
import random
import pandas

# List Comprehensions
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

doubled_range = [i * 2 for i in range(1, 5)]
print(doubled_range)

# Conditional list Comprehensions
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Dictionary Comprehensions
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# Loops/Iteration with Pandas Dataframes

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Looping through Data Frames
student_data_frame = pandas.DataFrame(student_dict)
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)
