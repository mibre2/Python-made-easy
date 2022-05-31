# Prime Number: Only divisible by itself and 1
    # (2, 3, 5, 7, 11, 13, 17, 19, ...)

# Composite Number: Can be factored into smaller integers
    # (4=2x2, 6=2x3, 8=2x2x2, 9=3x3, ...)

# Unit: 1

#===============================

import math
import time

#===============================

# V1 Test al divisors from 2 through n-1
    # (Skip 1 and n since every number is divisble by itself and 1

def is_prime_v1(n):
    """"Return 'True' if 'n' is not prime"""
    if n == 1: 
        return False    # 1 is not prime
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# ==== Test Function ====
v1_time_start = time.time()

for n in range(1, 100000):
    print("V1", n, is_prime_v1(n))

v1_time_end = time.time()

#===============================

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False    # 1 is not prime 
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# ==== Time Function ====
v2_time_start = time.time()

for n in range(1, 100000):
    print("V2", n, is_prime_v2(n))

v2_time_end = time.time()

#===============================

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False    # 1 is not prime 
    
    # If it's even and not 2, then it's not prime.
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# ==== Time Function ====
v3_time_start = time.time()

for n in range(1, 100000):
    print("V3", n, is_prime_v3(n))

v3_time_end = time.time()

#===============================

# ==== Time Function Results ====
print("V1 Time required: ", v1_time_end - v1_time_start)
print("V2 Time required: ", v2_time_end - v2_time_start)
print("V3 Time required: ", v3_time_end - v3_time_start)
