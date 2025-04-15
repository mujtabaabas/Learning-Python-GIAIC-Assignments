def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:
            print(i, end=" ")  # Print on same line with space

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

# This provided line is required at the end
if __name__ == '__main__':
    main()
