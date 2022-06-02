# Functions without names are known as "Lambda" or 'Anonymous'
    # They mean the same thing 

# Suppose you want to write a function that computers "3x+1"
    # This would be your standard approach:
def f(x):
    return 3*x+1
print("Regular: ",f(2))    # If you input 2, you get the value 7

# If you do the same using Anonymous functions:
    # To create a lambda expression, use the "lambda" keyword followed by your inputs
    # Next, add your ":"
    # Finally, type your expression that will be returned
        # lambda <inputs>: <expression to be returned>
print("Lambda 1: ")
print(lambda x: 3*x+1, "\n")  # When outtputed, you get location due to lambda having no name

# Example 2: Multiply argument a with b and return result
# Give the lambda keyword a name
g = lambda x: 3*x+1
print("lambda 2: ")
print(g(2), "\n")

# Example 3: Lambda expression with multiple inputs
full_name = lambda fn, ln : "lambda 3: " + "\n" + fn.strip().title() + " " + ln.strip().title()
print(full_name(" leonhard", "EULER"), "\n")