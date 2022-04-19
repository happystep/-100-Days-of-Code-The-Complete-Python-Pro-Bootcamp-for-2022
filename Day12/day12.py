# Day 12 - Beginner - Scope & Number Guessing Game

# Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Gloal Scope

player_health = 10

def drink_potion():
    potion_strengh = 2
    print(player_health)

drink_potion()

# There is no Block Scope in Python

game_level = 3
enemies = ["Skeleton", "Zomebie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
