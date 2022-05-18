# Functions are blocks of code you can reuse unlimited amount of times.

def f():    # Function called "f" with no arguments
    pass    # "pass" means to do nothing

f() # Call function "f" with no arguments

#============================================================================

# Create a function that returns a string

def ping1(): # Function called "ping" with no argument
    return "Ping 1!"

print(ping1(), "\n")

#============================================================================

# Create a function that returns a string, then store the returned value in a variable

def ping2():
    return "Ping 2!"

x = ping2()      # Stores a return value in a variable called "x"
print(ping2(), "\n")

#============================================================================

# Import the math function
# Create a function with 1 argument that returns the volume of a sphere using the math module
# Volume of a sphere is V=4/3 (pi)(r)^3

# Imports the math module
import math

# Function that has an argument "r" for radius
def volume(r):  
    """Returns the volume of a sphere with radius r.""" # This comment is called a "docstring", it displays what the function is and how to use it.
    V = (4/3)*math.pi*r**3
    return V

print("Volume of sphere with radius 2: ", volume(2))    # The argument passed through the function volume is the integer 2.
print("Volume of sphere with radius 5: ", volume(5))

print(help(volume), "\n") # Displays docustring of "volume" function.

#============================================================================

# Create a function with 2 arguments that returns the area of a triangle usign the math module
# Area of a triangle is A = 1/2(b)(h)

# Function called "triangle_area" that takes arguments "b" for base and "h" for height.
def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    return (1.0/2.0)*b*h

print(triangle_area(3, 6))
print(help(triangle_area), "\n")

#============================================================================

# Create a function with "kwarg arguments" that converts height from inches to centimetres
# 1 inch = 2.54, 1 foot = 12 inches

# Function called "cm" with default values of 0 for arguments feet and inches.
def cm(feet = 0, inches = 0):
    """Converts a length from feet an inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return  inches_to_cm + feet_to_cm

# Call a function with kward arguments
cm(feet = 5)
cm(inches = 70)
cm(feet = 5, inches = 8)
cm(inches = 8, feet = 4)
