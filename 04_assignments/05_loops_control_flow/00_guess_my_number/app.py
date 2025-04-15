import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Continue until the guess is correct
    while guess != secret_number:
        if guess < secret_number:  # If guess is too low
            print("Your guess is too low")
        else:  # If guess is too high
            print("Your guess is too high")
        
        print()  # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    # If the guess is correct
    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
