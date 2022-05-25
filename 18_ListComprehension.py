# List comprehension offers a shorter syntax when you want 
# to create a new list based on the values of an existing list.

def nolistcomp_displaysquare():
    """
    Returns a list of the first 10 squared numbers
    without list comprehension.
    """
    squares = []
    for i in range(1, 11):
        squares.append(i ** 2)
    return squares

# With list comprehension, you can do all of that with 1 line of code
def listcomp_displaysquare():
    """
    Same as display square() except with list comprehension.
    """
    squares2 = [i ** 2 for i in range(1, 11)]
    return squares2

print("No List comprehension squares: ", nolistcomp_displaysquare(), "\n", "=" * 36)
print("List comprehension squares: ", listcomp_displaysquare(), "\n", "=" * 36)

#=======================================================================

def listcomp_displayremainders():
    """
    Returns a list of remainders when dividing 
    the first 10 squares by 5.
    """
    remainders5 = [x ** 2 % 5 for x in range(1, 11)]
    return remainders5

print("Remainders: ", listcomp_displayremainders(), "\n", "=" * 36)

#=======================================================================

# list comprehension but with an if statement

# Suppose we have a list of movies and we want 
# to find movies that start with the letter "g".

def nolistcomp_movie():
    movies = ["Star Wars", "Ghandi", "Rio", "Groundhog Day", "Waste Deep", "Great Pretender"]
    
    gmovies = []    # Make an empty list of "G" starting movies

    for prefix in movies:   # Loop over all movies in the list
        if prefix.startswith("G"):  # If first index in the string is "G"
            gmovies.append(prefix)  # Append that item to "gmovies" list
    return gmovies

def listcomp_movie():
    movies = ["Star Wars", "Giovanni", "Rio", "Diablo", "Garfield", "Garden of Sinners"]

    gmovies = [prefix for prefix in movies if prefix.startswith("G")]
    return gmovies

print("No list comprehension movie: ", nolistcomp_movie(), "\n", "=" * 36)
print("List comprehension movie: ", listcomp_movie(), "\n", "=" * 36)
