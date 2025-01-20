
attempt = 0  # Initialize the attempt counter to 0
max_attempts = 3  # Set the maximum number of attempts
password_length = 3  # Set the required length for the password (3 characters)

while attempt < max_attempts:  # Run the loop while attempts are less than max_attempts
    password = input("Type your password: ")  # Get user input for the password

    # Check if the password is not exactly 3 characters
    if len(password) != password_length:
        print(f"Password must be exactly {password_length} characters.")  # Inform the user about the length requirement
        continue  # Skip this attempt and ask for the password again without counting it as an attempt

    # Check if the entered password is correct
    elif password == 'xyz':
        print("Access granted!")  # If password is correct, print "Access granted!"
        break  # Exit the loop since the correct password was entered

    else:  # If the password is incorrect and its length is valid
        attempt += 1  # Increment the attempt counter by 1
        if attempt < max_attempts:  # If attempts are still remaining
            print(f"Wrong password. {max_attempts - attempt} attempts left")  # Show remaining attempts
        else:  # If no attempts are left
            print("You have used all attempts. Access denied.")  # Inform the user that access is denied



