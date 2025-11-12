# Day 8 Practice – Find the Greatest of Four Numbers

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

# Using conditional statements to find the greatest number
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
    greatest = num4

print(f"The greatest number is: {greatest}")
