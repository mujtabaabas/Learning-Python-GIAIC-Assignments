import random  # Import the random library to simulate rolling dice

# Number of sides on each die
NUM_SIDES = 6

def main():
    # Simulate rolling the dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Ensure the main function is called when running the script
if __name__ == '__main__':
    main()
