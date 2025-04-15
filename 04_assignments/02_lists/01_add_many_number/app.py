def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    input_str: str = input("Enter numbers separated by spaces: ")
    numbers: list[int] = list(map(int, input_str.split()))
    sum_of_numbers: int = add_many_numbers(numbers)
    print("The sum of the numbers is:", sum_of_numbers)

if __name__ == '__main__':
    main()
