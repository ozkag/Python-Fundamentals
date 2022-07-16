import random

start_range = input("Enter the start of the range: ")

while not start_range.isdigit():
    print("Please enter a valid number.")
    start_range = input("Enter the start of the range: ")

stop_range = input("Enter the end of the range: ")

while not stop_range.isdigit() or int(stop_range) < int(start_range):
    print("Please enter a valid number.")
    stop_range = input("Enter the end of the range: ")

random_number = random.randint(int(start_range), int(stop_range))

while True:
    guess = input("Guess a number: ")
    attempts = 1

    while not guess.isdigit() or int(guess) != random_number:
        if not guess.isdigit():
            print("Please enter a valid number.")
            guess = input("Guess a number: ")

        else:
            guess = input("Guess a number: ")
            attempts += 1

    break

if attempts == 1:
    print(f"You guessed the number in {attempts} attempt")

else:
    print(f"You guessed the number in {attempts} attempts")
















    


