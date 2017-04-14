def alphabet_position(letter):
    """ receives a single character string and
        returns the 0-based index alphabet position
    """
    # calculate position based on lowercase characters
    letter = letter.lower()
    position = ord(letter) - 97
    return position


def rotate_character(char, rot):
    """ receives a single character string and an integer to rotate by
        returns the new char based on rotating to the right by rot
    """
    # return char if it is not a letter
    if not char.isalpha():
        return char
    # rotate position
    old_pos = alphabet_position(char)
    new_pos = (old_pos + rot) % 26
    # preserve original case
    if char.islower():
        new_pos += 97
    else:
        new_pos += 65
    # calculate and return new character
    char = chr(new_pos)
    return char


def reverse_character(char, rot):
    """ receives a single character string and an integer to rotate by
        returns the new char based on rotating to the left by rot
    """
    # return char if it is not a letter
    if not char.isalpha():
        return char
    # rotate position
    old_pos = alphabet_position(char)
    new_pos = (old_pos - rot) % 26
    # preserve original case
    if char.islower():
        new_pos += 97
    else:
        new_pos += 65
    # calculate and return new character
    char = chr(new_pos)
    return char
