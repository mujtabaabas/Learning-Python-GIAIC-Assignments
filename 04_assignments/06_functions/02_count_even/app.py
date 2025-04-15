def count_even(lst):
    """
    Prints the number of even numbers in the provided list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    """
    Prompts user to enter integers until Enter is pressed.
    Returns a list of those integers.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# Required to call main() when script is run
if __name__ == '__main__':
    main()
