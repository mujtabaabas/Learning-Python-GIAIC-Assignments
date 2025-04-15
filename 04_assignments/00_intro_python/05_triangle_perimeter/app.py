def main():
    # Get the 3 side lengths of the triangle from the user
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the perimeter
    print("The perimeter of the triangle is " + str(perimeter))

# Required to call the main() function
if __name__ == '__main__':
    main()
