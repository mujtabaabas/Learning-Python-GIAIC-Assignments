def main():
    # Prompt the user to enter a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")

# Required to call the main function when the script runs
if __name__ == '__main__':
    main()
