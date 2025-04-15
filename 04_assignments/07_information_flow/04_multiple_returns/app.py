def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return the data as a tuple
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    # Calling the function to get user data
    user_data = get_user_info()
    
    # Printing the received data
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
