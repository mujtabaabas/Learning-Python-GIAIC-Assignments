def is_odd(value: int):
    """
    Checks to see if a value is odd.
    Returns True if odd, False if even.
    """
    return value % 2 == 1

def main():
    for i in range(10, 20):  # Range from 10 to 19
        if is_odd(i):
            print(f"{i} odd", end=" ")
        else:
            print(f"{i} even", end=" ")

if __name__ == '__main__':
    main()
