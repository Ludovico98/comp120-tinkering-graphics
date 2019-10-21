"""Generates a random number and then prompts the
end-user to guess what that number is. It will
repeat until the end-user produces a correct guess.
Then, the script will terminate.
"""

import random
import enum

__author__ = "Michael Scott"
__copyright__ = "Copyright 2019, Falmouth University"
__license__ = "MIT"
__version__ = "1.0"
__url__ = "https://github.com/Adrir/comp120-tinkering-graphics"

MAX_VALUE = 100
MIN_VALUE = 0


class Guess(enum.Enum):
    """An enumeration for reporting the accuracy of
    guesses, and what the end-user should do next."""
    EQUAL = enum.auto()
    LOWER = enum.auto()
    HIGHER = enum.auto()


class Error(enum.Enum):
    """An enumeration for identifying types of error."""
    NOT_A_DIGIT = enum.auto()
    OUTSIDE_RANGE = enum.auto()
    UNKNOWN = enum.auto()


# This message dict will store all messages to send to the end-user
# to avoid entangling the main loop with literals. Use enum objects
# and string literals as keys.
MESSAGE = {
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
    """Print the message associated with the identifier.

    Args:
        message_id: the id of message in the MESSAGE dict (default Error.UNKNOWN),
            could be a string, an Error enum, or a Guess enum.
    """

    print(MESSAGE[message_id])


def check_guess(target_number, guessed_number):
    """Check if the guessed number is correct, and return an indication
    of whether it is higher, lower, or equal.

    Args:
        target_number (int): the number to be guessed
        guessed_number (int): the number the end-user has just guessed
    Returns:
        Guess enum object.
    """

    assert(isinstance(target_number, int) and isinstance(guessed_number, int))

    information = None
    if target_number == guessed_number:
        information = Guess.EQUAL
    elif target_number > guessed_number:
        information = Guess.HIGHER
    else:
        information = Guess.LOWER

    return information


def validate(expected_integer):
    """Check if the guessed number is correct, and return an indication
    of whether it is higher, lower, or equal.

    Args:
        expected_integer (str): an integer input by the end-user to
            be checked
    Returns:
        If valid, an int. Error enum object otherwise.
    """

    return_value = None

    try:
        expected_integer = int(expected_integer)

        if MIN_VALUE < expected_integer <= MAX_VALUE:
            return_value = expected_integer
        else:
            return_value = Error.OUTSIDE_RANGE

    except ValueError:
        return_value = Error.NOT_A_DIGIT

    return return_value


def main():
    """Main loop for program execution"""

    random_number = random.randrange(MIN_VALUE, MAX_VALUE + 1)              # Include max number
    print_message("Generated_Number")

    guessed = False
    while not guessed:

        print_message("Request_Input")
        user_input = input()
        validated_user_input = validate(user_input)
        if isinstance(validated_user_input, Error):
            print_message(validated_user_input)
            continue

        outcome = check_guess(random_number, validated_user_input)
        if outcome is Guess.EQUAL:
            guessed = True

        print_message(outcome)


if __name__ == "__main__":
    main()
