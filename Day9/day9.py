# Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictioanry
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Create an empty dictioary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictioanry
# this is only the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting Lists and Diccionaries

capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nest a Dictioanry in a Dictionary

travel_log = {
    "France": {"Cities_Visited" : ["Paris", "Lille", "Dijon" ], "total_visits" : 12},
    "Germany": {"Cities_Visited" : ["Berlin", "Hamburg", "Stuttgart" ], "total_visits" : 5},
}

# Nest a Dictionary in a List

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
