def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2


def test_average():
    """
    Runs simple tests to validate the average function.
    """
    assert average(0, 10) == 5
    assert average(10, 10) == 10
    assert average(-10, 10) == 0
    assert average(2.5, 7.5) == 5
    print("✅ All tests passed!")


def main():
    print("📊 Welcome to the Average Calculator!\n")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        avg = average(a, b)
        print(f"\n🧮 The average between {a} and {b} is: {avg}")

        # Optional test call (can be removed in production)
        print("\n🧪 Running internal tests...")
        test_average()

    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")


# Required to call main function
if __name__ == '__main__':
    main()
