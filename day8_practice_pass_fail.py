# Day 8 Practice – Check if a Student is Pass or Fail

# Taking marks input for 3 subjects
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

# Calculating total and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100  # Assuming each subject is out of 100

# Checking conditions
if (percentage >= 40) and (sub1 >= 30) and (sub2 >= 30) and (sub3 >= 30):
    print(f"Congratulations! You passed with {percentage:.2f}% marks.")
else:
    print(f"Sorry, you failed. Your total percentage is {percentage:.2f}%.")
