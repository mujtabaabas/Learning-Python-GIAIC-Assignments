def print_multiple(message: str, repeats: int):
    # Prints the message the specified number of times
    for i in range(repeats):
        print(message)

def main():
    # Prompt user for a message and number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    # Call the function to print the message
    print_multiple(message, repeats)

# This line is required to call the main function when the script runs
if __name__ == '__main__':
    main()
