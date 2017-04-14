def get_initials(fullname):
    """Given a person's name, return the person's initials (uppercase)"""
    initials = fullname[0]
    for i in range(len(fullname)-1):
        if fullname[i] == " ":
            initials = initials + fullname[i+1]
    initials = initials.upper()
    return initials


def main():
    name = input("What is your name?\n")
    print(get_initials(name))

if __name__ == "__main__":
    main()
