# Prompt user to enter an integer.
# The value of the integer will be "user_input2"
# Due to "input" function taking "user_input2" as a string, we must convert it to integer
number = int(input("Please enter a number: "))

# If number is divisible by 2 display the number is even.
if number % 2 == 0: # "%" returns the remainder.
    print("Your number is even.")
# Display the number is odd.
else:
    print("Your number is odd.")

# If user inputs string instead of a number
    # Error line will display where the code failed
    # This causes a "ValueError"
    # Due to no instructions on how to handle the error, program will fail
    