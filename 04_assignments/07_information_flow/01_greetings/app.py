def greet(name):
    # Function to return the greeting message
    return "Greetings " + name + "!"

def main():
    # Get the user's name
    name = input("What's your name? ")
    
    # Call the greet function and print the result
    print(greet(name))

# This line is required to call the main() function
if __name__ == '__main__':
    main()
