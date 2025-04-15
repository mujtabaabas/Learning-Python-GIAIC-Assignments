def main():
    # Dictionary of fruits with their respective prices
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize the total cost
    
    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the current fruit
        # Ask the user how many of this fruit they want to buy
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        # Add the cost of this fruit to the total cost
        total_cost += (price * amount_bought)
    
    # Print the total cost
    print("Your total is $" + str(total_cost))


# Python boilerplate to run the main function
if __name__ == '__main__':
    main()
