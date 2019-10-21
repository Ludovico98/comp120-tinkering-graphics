import random

EQUAL = 1
LOWER = 2
HIGHER = 3
MAX_VALUE = 100
MIN_VALUE = 0


def correct_guess(target_number, user_input_number):
    if target_number == user_input_number:
        return EQUAL
    elif target_number > user_input_number:
        return HIGHER
    elif target_number < user_input_number:
        return LOWER


def is_valid(expected_integer):
    if not expected_integer.isdigit():
        return False
    else:
        expected_integer = int(expected_integer)

    if not expected_integer < MAX_VALUE:
        return False
    if not expected_integer >= MIN_VALUE:
        return False

    return True


random_number = random.randrange(MIN_VALUE, MAX_VALUE + 1)
print("Random number has been generated:", random_number)

guessed = False
while not guessed:

    user_input = input("Your guess please: ")
    if is_valid(user_input):
        guess = int(user_input)
    else:
        print("Please use an integer between",
              str(MIN_VALUE),
              "and",
              str(MAX_VALUE)
              )
        continue

    outcome = correct_guess(random_number, guess)
    if outcome == EQUAL:
        guessed = True
        print("You win!")
        print("Well done!")
    elif outcome == HIGHER:
        print("Try one more time, a bit higher")
    elif outcome == LOWER:
        print("Try one more time, a bit lower")