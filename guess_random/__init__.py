import random
import enum

MAX_VALUE = 100
MIN_VALUE = 0


class Guess(enum.Enum):
    EQUAL = enum.auto()
    LOWER = enum.auto()
    HIGHER = enum.auto()


class Error(enum.Enum):
    NOT_A_DIGIT = enum.auto()
    OUTSIDE_RANGE = enum.auto()
    UNKNOWN = enum.auto()


message = {
    Guess.EQUAL:  "You win!\nWell done!",
    Guess.LOWER: "Try one more time, a bit lower!",
    Guess.HIGHER: "Try one more time, a bit higher!",
    Error.NOT_A_DIGIT: "That wasn't a number! Please enter a whole number!",
    Error.OUTSIDE_RANGE:
        "Please use an integer between {0} and {1}".format(str(MIN_VALUE), str(MAX_VALUE)),
    Error.UNKNOWN: "An unknown error occurred, please reset!",
    "Generated_Number": "Random number has been generated",
    "Request_Input": "Your guess please: "
}


def print_message(message_id=Error.UNKNOWN):
    print(message[message_id])


def check_guess(target_number, guessed_number):
    if target_number == guessed_number:
        return Guess.EQUAL
    elif target_number > guessed_number:
        return Guess.HIGHER
    elif target_number < guessed_number:
        return Guess.LOWER


def validate(expected_integer):
    try:
        expected_integer = int(expected_integer)
    except ValueError:
        return Error.NOT_A_DIGIT

    if MIN_VALUE < expected_integer <= MAX_VALUE:
        return expected_integer
    else:
        return Error.OUTSIDE_RANGE


random_number = random.randrange(MIN_VALUE, MAX_VALUE + 1)              # Include max number
print_message("Generated_Number")

guessed = False
while not guessed:

    print_message("Request_Input")
    user_input = input()
    validated_user_input = validate(user_input)
    if type(validated_user_input) is Error:
        print_message(validated_user_input)
        continue

    outcome = check_guess(random_number, validated_user_input)
    if outcome is Guess.EQUAL:
        guessed = True

    print_message(outcome)