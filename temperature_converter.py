def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Taking user input
choice = input("Convert from (C)elsius or (F)ahrenheit? ").lower()

if choice == "c":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")

elif choice == "f":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")

else:
    print("Invalid choice. Please enter C or F.")
