def main():
    lst = []  # Make an empty list to store things in

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val)  # Add val to the list
        val = input("Enter a value: ")  # Get the next value

    print("Here's the list:", lst)


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
