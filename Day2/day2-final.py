print("Welcome to the tip calculator.\n")

total = int(input("What was the total bill? $"))

percen = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

total_tip = total + (total * (percen/100))

# per_person = round(total_tip/people, 2)
per_person = "{:.2f}".format(total_tip/people)

print(f"Each person should pay: ${per_person}")
