def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False  # This is returned if the condition isn't met

def main():
    # Example usage (you can modify this to test)
    print(in_range(5, 1, 10))  # Expected: True
    print(in_range(0, 1, 10))  # Expected: False

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
