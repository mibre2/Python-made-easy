# Python has a built-in package called "json", which can be used to work with JSON data.

import json     # import the json module

# If you have a JSON string, you can parse it by using the "json.loads() method.
    # The result will be a Python dictionary.

def json_example_1():
    """Converts from JSON to Python"""

    # Some JSON
    x = '{"name":"John", "age":"31", "city":"Baltimore"}'

    # Parse x:
    y = json.loads(x)

    # The result is a Python dictionary:
    print(y["name"])
    print(y["age"])
    print(y["city"])

#==========================================================================================================

# If you have a Python object, you can convert it into a JSON string by using the "json.dumps()"" method.

def json_example_2():
    """Convert from Python to JSON"""
    x = {
        "name":"Miles",
        "age":14,
        "city":"New York"
    }

    # Converts into JSON
    y = json.dumps(x)

    # The result is a JSON string:
    print(y)

#==========================================================================================================

def json_example_3():
    """
    Convert Python objects into JSON strings, and print the values.
    You can convert Python objects of the following types into JSON strings:
        dict, list, tuple, string, int, float, True, False, and None.
    """
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

#==========================================================================================================
def json_example_4():
    pass
#==========================================================================================================

# Code Execution begins here
def main():
    print("JSON Example 1: ")
    json_example_1()
    print()

    print("JSON Example 2: ")
    json_example_2()
    print()

    print("JSON Example 3: ")
    json_example_3()
    print()

main()
