# Display the 3 types of numbers in Python.

# ints (Means integers)
a = 496
print("a =", a, "=", type(a), "\n")

# floats (Means numbers with decimals)
b = 12.2
print("b =", b, "=", type(b), "\n")

# complex (j = sqrt(-1))
# Python uses j to represent complex numbers
c = 2-6.2j
print("c =", c, "=", type(c))
print(c.real)   # Python stores complex numbers in floats
print(c.imag)
