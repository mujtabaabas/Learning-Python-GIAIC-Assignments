import random

N_NUMBERS : int = 10  # Number of random numbers to generate
MIN_VALUE : int = 1    # Minimum value for the random number
MAX_VALUE : int = 100  # Maximum value for the random number

def main():
    # Generate 10 random numbers between MIN_VALUE and MAX_VALUE
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Print each random number on the same line

if __name__ == '__main__':
    main()
