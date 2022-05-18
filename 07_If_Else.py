# Prompt user to enter a string.
# The value of the string will be "user_input"
user_input1 = input("Please enter a string: ")

# If length of user input is < 6, prompt user to enter a longer string
if len(user_input1) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")

# If user inputs a number > 6, program ends due to no instructions.
