# Day 8 Practice – Check Username Length

# Taking username as input from the user
username = input("Enter your username: ")

# Checking if the username has less than 10 characters
if len(username) < 10:
    print("⚠️ Username contains less than 10 characters.")
else:
    print("✅ Username is 10 or more characters long.")
