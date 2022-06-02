# The "sort()" method sorts list in ascending order by default.
# You can also make a function to deside the sorting criteria(s).

# Syntax: list.sort(reverse = True | key = myFunc)

# Parameter Values
    # reverse: Optional. "reverse=True" will sort in descending order.
        # Default is "reverse=False"
    # key: Optional. Functio nto specify the sorting criteria(s)

# Example 1: sorting a list of integers in ascending order
num_list = [1,2,3,4,56,5,2,4,5] # Initial list of numbers
num_list.sort() # List sorted in ascending order
print("Ascending sort: ", "\n", num_list, "\n")

# Example 2: Sort a list of integers in descending order
num_list2 = [1,2,3,4,56,5,2,4,5] # Initial list of numbers
num_list2.sort(reverse=True) # List sorted in ascending order
print("Descending sort: ", "\n", num_list2, "\n")

# Example 3: Sort the list by length of values
def val_length(names):
    return len(names)

names = ['Michael', 'Raphael', 'Donetello', 'Leonardo']
names.sort(key=val_length)
print("Length of value sort: ", "\n", names, "\n")

# Example 4: Sort a list of dictionaries based on the "year" value of dictionaries

def dict_sort(cars):
    return cars['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=dict_sort)
print("Dictionary value sort: ", "\n", cars)
