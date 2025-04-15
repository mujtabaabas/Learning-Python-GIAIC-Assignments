ADULT_AGE = 18  # U.S. age at which a person is considered an adult

def is_adult(age: int):
    """
    Returns True if age is greater than or equal to ADULT_AGE, else False.
    """
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Ask for the age input and convert it to integer
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

# This line is required to call the main() function
if __name__ == "__main__":
    main()
