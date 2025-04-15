def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is also divisible by 100, check if it is divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call the main function when "run", no need to edit anything below!
if __name__ == '__main__':
    main()
