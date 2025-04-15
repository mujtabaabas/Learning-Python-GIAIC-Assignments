import random

# Adjust this to control how likely it is to stop early (e.g., 0.2 = 20% chance to stop at each number)
DONE_LIKELIHOOD = 0.2

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Ends function early if done() returns True
        print(curr_num, end=" ")

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

if __name__ == '__main__':
    main()
