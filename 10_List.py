# List are builtin data structures for storing and accessing objects in a specific sequence

# Two different way sot build a list.

# List constructor:
example = list()

# Use  brackets "[]":
example = []

# Prepopulate list with values of prime numbers
primes = [2, 3, 5, 6, 11, 13]
print("Original primes list: ", primes, "\n")

# Add values to the end of the list with the "append" method 
primes.append(17)
primes.append(19)
print("Updated primes list: ", primes, "\n")    # NOTICE list preserves the order of the data

#=======================================================================

# Access element within list by its index.
# You do this by writing the list name followed by the index in brackets "[]".
print("Index 0: ", primes[0])           # Prints 2 because that is index 0 in the list.
print("Index 1: ", primes[1])           # Prints 3 because that is index 1 in the list.
print("Index 3: ", primes[3])           # Prints 6 because that is index 3 in the list.
print("Index -1: ", primes[-1])         # Prints 19 because -1 index is the end of the list after append.
print("Index -2: ", primes[-2], "\n")   # Print 17 becasue -2 index continues to move to the left of the list after append.

# Access values within list by "Slicing"
# Slicing allows us to retrieve A RANGE of values from a list.
# This is achieved by specifying a starting index and ending index in brackets "[start:stop]"
print("Indexes 2-5: ", primes[2:5])         # Prints numbers 5,6,and 11 because those are the vaules of indexes 2-5. NOTICE index 5 IS NOT INCLUDED in printed list.and
print("Indexes 0-7: ", primes[0:7], "\n")   # Prints numbers 2, 3, 5, 6, 11, 13, and 17

#==================================================================

# List can contain integers, booleans, strings, floats, and other list
example2 = [128, True, "Hello", 2.17, [64, False]]
print("Multiple data type list: ", example2, "\n") # Prints list containing multiple data types.

# List can contain duplicate values
rolls = [4, 7, 2, 8, 4, 2, 7, 8 ]
print("Duplicate values list: ", rolls, "\n") # Prints list with duplicate values.

# Multiple different list can be combined
numbers = [1,2,3]
letters = ['a', 'b', 'c']
numbers_and_letters = numbers + letters                     # List combnined in numbers -> letters order.         
letters_and_numbers = letters + numbers                     # List combined in letters -> numbers order.
print("Combined list: ", numbers_and_letters)               # Prints combined list.
print("Flipped combined list: ", letters + numbers, "\n")   # Prints list with numbers and letters flipped.

# Reverse the combined list using the "list.reverse" method
numbers.reverse()               # Reverse the numbers list using the "list.reverse" method   
letters.reverse()               # Reverse the letters list using the "list.reverse" method
numbers_and_letters.reverse()   # Reverse numbers_and_letters list using "list.reverse" method.
letters_and_numbers.reverse()   # Reverse letters_and_numbers list using "list.reverse" method.

print("Numbers reversed: ", numbers)
print("Letters reversed: ", letters)
print("Numbers & letters reversed: ", numbers_and_letters)  
print("Letters & numbers reversed: ", letters_and_numbers)  
