# Day 6 – Dictionaries & Sets

# Dictionary Example
student = {
    "name": "Abdullah",
    "age": 18,
    "course": "Python"
}

print("Student name:", student["name"])

# Adding a new key-value pair
student["city"] = "Lahore"
print("Updated student:", student)

# Set Example
fruits = {"apple", "banana", "orange"}
fruits.add("mango")
print("Fruits set:", fruits)

# Removing a value
fruits.discard("banana")
print("After removing banana:", fruits)
