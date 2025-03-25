import random

# Statement: Guess a random number between 1 and max_limit.


def guess(max_limit):
    """Machine Guessed a random number between 1 and max_limit."""
    random_number = random.randint(1, max_limit)

    guess = 0  # Guessed number initialized

    # Loop will run until the guessed number is correct
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {max_limit}: "))
        if guess < random_number:
            print("Too low! Try again!")
        elif guess > random_number:
            print("Too high! Try again!")

    print(f'Congrats! you guessed the number {random_number}')


guess(int(input(
    # Get max limit from user and pass it to the function
    'Please enter max limit for the machine to generate for guess game: ')))
