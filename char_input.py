name = input("Enter your name: ")
age = input("Enter your age: ")

years_until_100 = 100 - int(age)
days_until_100 = years_until_100 * 365

times = int(input("Type the amount of copies you want to print: "))

print(times * f"Hello {name}, you are {age} years old and will be 100 in {years_until_100} years\n")