'''1. Modify your greeting program so that if the user does not enter a name (i.e. they
 just press enter), the program responds "Hello, Stranger!". Otherwise it should print
 a greeting with their name as before.'''

user_password = input("Please enter a new password: ")
confirm_password = input("Please confirm your password: ")
if user_password == confirm_password:
    if len(user_password) >= 8 and len(user_password) <= 12:
        print("Password Set")
    else:
        print("Error: Password must be between 8 and 12 characters.")

else:
    print("Error: Passwords do not match.")