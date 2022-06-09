user_number = int(input("Enter a number: "))
denom = int(input("Enter a denominator: "))

if user_number % 2 == 0:
    print("Your number is an even number.")
else:
    print("Your number is an odd number.")

if user_number % denom == 0:
    print(f"Your number can be divided by {denom}.")
else:
    print(f"Your number cannot be divided by {denom}.")

if user_number % 4 == 0:
    print("Your number is a multiple of 4.")