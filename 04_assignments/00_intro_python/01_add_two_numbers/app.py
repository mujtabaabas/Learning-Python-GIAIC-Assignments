def main():
    print("This program adds two numbers.")

    # Prompt and convert the first input to an integer
    num1 = int(input("Enter the first number: "))

    # Prompt and convert the second input to an integer
    num2 = int(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Display the result
    print("The total is " + str(total) + ".")

# Required to call the main function when the script runs
if __name__ == '__main__':
    main()
