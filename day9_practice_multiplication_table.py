# Day 9 Practice – Multiplication Table using For Loop

# Taking input from the user
num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table of {num}:\n")

# Using for loop to print table from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
