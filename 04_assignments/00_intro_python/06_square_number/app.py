def main():
    # Prompt the user for a number and convert it to float
    num = float(input("Type a number to see its square: "))

    # Calculate and print the square
    print(str(num) + " squared is " + str(num ** 2))

# Required to call the main() function
if __name__ == '__main__':
    main()
