# Tuples use "()".
# List/arrays use "[]".

# List example
list_prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
tuple_perfect_squares = (1, 4, 9, 16, 25, 36)

'''# Display lengths 
print("# Primes = ", len(list_prime_numbers))
print("# Squares = ", len(tuple_perfect_squares), "\n")

print(80*"-", "\n")

# Iterate over both sequences
for p in list_prime_numbers:
    print("Primes: ", p)

print("\n")

for s in tuple_perfect_squares:
    print("Square: ", s)

print(80*"-", "\n")

# Compare list and tuple methods
print("List methods")
print(dir(list_prime_numbers))  # NOTICE: List have more methods than tuples, therefore they take more memory.

print(80*"-", "\n")

print("Tuple methods")
print(dir(tuple_perfect_squares), "\n")

print(80*"-", "\n")

'''

# Import sys module
import sys

# Use the "getsizeof" method in "sys" module to display the size of list vs tuple 
list_eg = [1,2,3,"a","b","c",True, 3.14159]
tuple_eg = (1,2,3,"a","b","c",True, 3.14159)

print("List size: ", sys.getsizeof(list_eg))
print("Tuple size: ", sys.getsizeof(tuple_eg))