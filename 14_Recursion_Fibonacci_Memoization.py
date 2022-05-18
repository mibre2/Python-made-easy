# Fibonnaci Sequence: 1, 1, 2, 3, 5, 8, 13, 21
# Fibonnaci Explained: 0+1=1, 1+1=2, 2+3=5, 3+5=8, 5+8=13, 8+13=21, ect
# You add previous results to the list until you find desired results.

# Write a function to return nth term of Fibonnaci Sequence.
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1+2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
        
