AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user input

    # Keep prompting the user until they type the correct affirmation
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

# This line calls the main() function when the script is run
if __name__ == '__main__':
    main()
