import math  # Import the math library to use the sqrt function

def main():
    # Get the lengths of the two perpendicular sides from the user
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse (BC) using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Output the result
    print("The length of BC (the hypotenuse) is:", bc)

# Required to call the main() function
if __name__ == '__main__':
    main()
