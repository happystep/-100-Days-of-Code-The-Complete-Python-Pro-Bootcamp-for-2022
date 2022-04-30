# Day 24 - Intermediate - Files, Directories, and Paths
# It seems like today is a day when we revisit code from a previous day.

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# another way of opening, where we don't have to close

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# We can also write
with open("my_file.txt", mode="a") as file:
    file.write("New text")

# You can also create a file when it doesn't exist
with open("new_file.txt", mode="a") as file:
    file.write("New text")
