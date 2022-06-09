import random

start = input("Enter the start of the range: ")
while not start.isdigit():
    print("Please enter a valid number.")
    start = input("Enter the start of the range: ")

stop = input("Enter the end of the range: ")
while not stop.isdigit():
    print("Please enter a valid number.")
    stop = input("Enter the end of the range: ")

while stop < start:
    print("Please enter a valid number.")
    stop = input("Enter the end of the range: ")
    

number_of_guesses = 0
random_num = random.randint(int(start), int(stop))


while True:
    user_guess = input("Guess a number: ")
    while not user_guess.isdigit():
        print("Please enter a valid number.")
        user_guess = input("Guess a number: ")

    number_of_guesses += 1
    if int(user_guess) == random_num:
        break

if number_of_guesses == 1:
    print(f"You guessed the number in 1 attempt")
else:
    print(f"You guessed the number in {number_of_guesses} attempts")