MAX_TERM_VALUE: int = 10000

def main():
    # Initialize the first two Fibonacci numbers
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    
    # Print Fibonacci numbers as long as they are <= MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term
        term_after_next = curr_term + next_term  # Next Fibonacci number
        curr_term = next_term  # Move to the next term
        next_term = term_after_next  # Update the next term

# Python boilerplate to execute the program
if __name__ == '__main__':
    main()
