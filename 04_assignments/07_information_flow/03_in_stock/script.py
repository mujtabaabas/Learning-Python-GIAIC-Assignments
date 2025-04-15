def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This function returns the number of fruits Sophia has in stock.
def num_in_stock(fruit):
    """
    Returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0  # This fruit is not in stock.

# This line is required to run the program
if __name__ == '__main__':
    main()
