# Use when working with data and the order or frequency doesn't matter.

# Empty set called "example"
example = set()

# Add objects to set using builtin "add" method
example.add(42) # Sets DO NOT contain duplicate elements
example.add(42)
example.add(False)
example.add(3.14159)
example.add("String here")

# Display objects within the set
print("example")
print("-------")
print(example)

# Display the number of objects in the set
print("Length of set: ", len(example), "\n")

example.remove(42)  # Remove objects from the set using builtin "remove" method 
print("Update set after removing 42")
print("--------------------------------------")
print(example, "\n")      # Displays the updated set

#================================================================

# Create a set that already contain objects

exmaple2 = set([28, True, 2.784, "Helium"])
print("exmaple2")
print("--------")

print(exmaple2)
print("Length of set: ", len(exmaple2), "\n")

#================================================================

# Clear out all the objects in the set

example3 = set([28, True, False, "Hardware Store"])
print("exmaple3")
print("--------")
print(example3, "\n") # Displays the original set

print("Set after clearing")
print("------------------")
example3.clear()  # Displays the updated set
print(example3)

print("Length of set: ", len(example3), "\n")
