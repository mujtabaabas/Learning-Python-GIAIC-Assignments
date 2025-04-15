def subtract_seven(num):
    num = num - 7
    return num

def main():
    num = 7  # Initialize num with 7
    num = subtract_seven(num)  # Call the subtract_seven function
    print("this should be zero:", num)  # Print the result

# Call the main function to run the program
if __name__ == '__main__':
    main()
