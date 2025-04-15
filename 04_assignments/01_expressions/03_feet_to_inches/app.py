# Conversion factor: there are 12 inches in 1 foot
INCHES_IN_FOOT = 12

def main():
    # Prompt the user to enter the number of feet
    feet = float(input("Enter number of feet: "))  # Convert input to a float

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

    # Display the result
    print("That is", inches, "inches!")

# Required to call the main() function
if __name__ == '__main__':
    main()
