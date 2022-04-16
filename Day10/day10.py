# Day 10 - Beginner - Functions with Outputs

# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and  last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formatred_l_name = l_name.title()

    return f"{formated_f_name} {formatred_l_name}"

formated_string = format_name("angela", "ANGELA")

print(formated_string)

print(format_name(input("What is your first_name? "), input("What is your last name ?")))
