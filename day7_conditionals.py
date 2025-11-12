# Day 7 – Conditional Expressions

age = 18

# Basic if-else
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible yet.")

# Using elif
marks = 75
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Keep improving!")

# Conditional Expression (Ternary Operator)
temperature = 30
weather = "Hot" if temperature > 25 else "Cool"
print("Weather is:", weather)
