def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i
        numbers[i] = elem_at_index * 2  # Replace with the element doubled

    print(numbers)  # Output: [2, 4, 6, 8]

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
