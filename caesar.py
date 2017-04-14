from helpers import alphabet_position, rotate_character, reverse_character
from sys import argv, exit


def encrypt(text, rot):
    """ receives a string, rotates the characters by the the integer rot and
        returns the new string
    """
    if type(rot) != int:
        rot = int(rot)
    # if text is not a string, return text
    if type(text) is not str:
        return text
    # encrypt and return the new string
    new_string = ""
    for i in range(len(text)):
        new_string += rotate_character(text[i], rot)
    return new_string


def decrypt(text, rot):
    """ receives a string, rotates the characters by the the integer rot and
        returns the new string
    """
    if type(rot) != int:
        rot = int(rot)
    # if text is not a string, return text
    if type(text) is not str:
        return text
    # encrypt and return the new string
    new_string = ""
    for i in range(len(text)):
        new_string += reverse_character(text[i], rot)
    return new_string


def user_input_is_valid(cl_args):
    # ensure that variable argv[1] is legal and return a Boolean
    if len(cl_args) < 2 or not cl_args[1].isdigit():
        return False
    return True


def main():
    if not user_input_is_valid(argv):
        print("invalid command line argument, usage: python3 caesar.py n")
        exit()
    message = input("Type a message:")
    print(encrypt(message, argv[1]))


if __name__ == "__main__":
    main()
