# Day 9 – Loops in Python

# ------- FOR LOOP -------
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# ------- WHILE LOOP -------
print("\nWhile loop counting down from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1

# ------- LOOP WITH LIST -------
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# ------- BREAK & CONTINUE -------
print("\nBreak and Continue Example:")
for num in range(1, 10):
    if num == 5:
        continue  # skip 5
    if num == 8:
        break     # stop at 8
    print(num)
