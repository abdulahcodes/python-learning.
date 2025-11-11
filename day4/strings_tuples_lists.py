# Day 4: Strings, Tuples & Lists
# Author: Abdullah

# --- STRINGS ---
name = "Abdullah"
greeting = f"Hello, {name}! Welcome back to Python learning."
print(greeting)

# String slicing
print("First 3 letters of your name:", name[:3])
print("Reversed name:", name[::-1])

# --- LISTS ---
fruits = ["apple", "banana", "mango"]
print("\nFruits List:", fruits)
fruits.append("orange")
print("After adding orange:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)

# --- TUPLES ---
coordinates = (33.6844, 73.0479)  # Example: Islamabad coordinates
print("\nCoordinates Tuple:", coordinates)

# Tuple unpacking
lat, long = coordinates
print(f"Latitude: {lat}, Longitude: {long}")
