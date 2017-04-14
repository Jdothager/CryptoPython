from helpers import alphabet_position, rotate_character, reverse_character


def encrypt(text, key):
    """ receives a string, text, to be encrypted and a string, key, to set the rotation by
        returns a new string
    """
    # if text is not a string, return text
    if type(text) is not str:
        return text
    # encrypt and return the new string
    new_string = ""
    key_counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            key_pos = key_counter % len(key)
            rot = alphabet_position(key[key_pos])
            new_string += rotate_character(text[i], rot)
            key_counter += 1
        else:
            new_string += text[i]
    return new_string


def decrypt(text, key):
    """ receives a string, text, to be decrypted and a string, key, to reverse the rotation by
        returns a new string
    """
    # if text is not a string, return text
    if type(text) is not str:
        return text
    # encrypt and return the new string
    new_string = ""
    key_counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            key_pos = key_counter % len(key)
            rot = alphabet_position(key[key_pos])
            new_string += reverse_character(text[i], rot)
            key_counter += 1
        else:
            new_string += text[i]
    return new_string


def main():
    message = input("Type a message:\n")
    key = input("Encryption key:\n")
    print(encrypt(message, key))


if __name__ == "__main__":
    main()