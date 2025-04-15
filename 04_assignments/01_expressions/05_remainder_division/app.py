def main():
    # Get the numbers for division from the user
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform the integer division (quotient) and calculate the remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Output the result
    print("The result of this division is", quotient, "with a remainder of", remainder)

# Required to call the main() function
if __name__ == '__main__':
    main()
