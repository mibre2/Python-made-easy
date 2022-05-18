# Python interactive help features 

# dir() returns the directory.
print("dir() directory")
print("---------------")
print(dir(), "\n")

# dir('__builtins__') returns a list of builtin functions.
print("dir(__builtins__) directory")
print("---------------------------")
print(dir('__builtins__'), "\n")

# To learn about function, you'd call one of the options the with "help" function.
# For this example, I'll call upon the "len" function using the "help" function.
print("help(len)")
print("---------")
print(help(len), "\n")

# Display a list of Modules.
# Modules are functions you would have to import.
print("help('modules')")
print("---------------")
help('modules')

# Import modules
# For this example, I'll import the "math" module.
import math

# to verify, check the directory
print("dir()")
print("-----")
print(dir(), "\n")    # You'll see your modules in the list of the directories

# Use the directory function to see what's in the "math" module
print("dir(math)")
print("---------")
print(dir(math), "\n")


# Use the help function to see what's in the "math.<function>" module
# For this example, I'll display what's in the "sqrt" function within the "math" module
print("help(math.sqrt)")
print("---------------")
print(help(math.sqrt), "\n")
