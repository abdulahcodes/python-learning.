# Day 8 Practice – Simple Spam Detector Program

# Taking comment input from the user
comment = input("Enter your comment: ")

# Converting comment to lowercase for easy checking
comment_lower = comment.lower()

# Checking for spam keywords
if ("make a lot of money" in comment_lower or
    "buy now" in comment_lower or
    "subscribe this" in comment_lower or
    "click this" in comment_lower):
    print("⚠️ This comment is spam!")
else:
    print("✅ This comment looks genuine.")
