def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # Stop input when the user enters a blank name
            break
        number = input("Number: ")
        phonebook[name] = number  # Store name and number in the phonebook

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook:")
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":  # Exit if blank name is entered
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")  # Name not found
        else:
            print(name + "'s number is: " + phonebook[name])  # Print the number for the given name


def main():
    phonebook = read_phone_numbers()  # Get the phonebook from the user
    print_phonebook(phonebook)  # Print all the phonebook entries
    lookup_numbers(phonebook)  # Allow the user to look up phone numbers


# Python boilerplate to execute the program
if __name__ == '__main__':
    main()
