def print_ones_digit(num):
    # Prints the ones digit of the number
    print("The ones digit is", num % 10)

def main():
    # Prompt user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the function to print the ones digit
    print_ones_digit(num)

# This provided line is required to call the main() function when script is run
if __name__ == '__main__':
    main()
