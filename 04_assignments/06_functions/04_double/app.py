def double(num: int):
    """
    Returns double the value of the input number.
    """
    return num * 2

# No need to edit beyond this point
def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
