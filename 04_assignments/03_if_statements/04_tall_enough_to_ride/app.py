MINIMUM_HEIGHT : int = 50  # arbitrary units :)

def tall_enough_extension():
    while True:
        # Ask the user for their height
        height_input = input("How tall are you? ")
        
        if height_input == "":
            # Stop if the user doesn't enter anything
            break
        
        # Convert the height to float and check if they are tall enough
        height = float(height_input)
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

def main():
    tall_enough_extension()

if __name__ == '__main__':
    main()
