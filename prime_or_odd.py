num = int(input("Enter a number: "))

# Check if odd
if num % 2 != 0:
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number.")

# Check if prime
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is also a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(f"{num} is not a prime number.")
