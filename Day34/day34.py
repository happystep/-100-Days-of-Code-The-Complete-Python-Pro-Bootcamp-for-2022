# Day 34 - Intermediate + API Practice - Creating a GUI Quiz app.

# Most of the work is in other files.

# Python Typing: Type Hints and Arrows ->

age: int
name: str
height: float
is_human: bool


def police_check(c_age: int) -> bool:
    if c_age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You pass")
else:
    print("You failed")
