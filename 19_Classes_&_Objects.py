import datetime
# To define a class you use the keyword "class" followed by the name of the class.
class User:
    # "pass" is a way to tell pythohn to do nothing. 
    # This is important because in order to have a class, there needs to be at least one line of code.
    pass

# Calls the class "user" by assigning a variable to it.
user1 = User()  # We call "user1" an "instance" or "object" of the "User" class.

# Assign data to the "instances" or "objects" of the "User" class.
user1.first_name = "John" 
user1.last_name = "Doe"

# print the user's first name and last name
print(user1.first_name)
print(user1.last_name, "\n")

# Stand alone variables to assign another user to first name and last name.
# These values are not attached to a user object.
first_name = "Arthur"
last_name = "Fleck"

# print the stand alone variables and class objects with same names.
# Even when using the same variable name, two different values appear due to them being seperate.
print("Class name: ", user1.first_name, user1.last_name)
print("Stand alone name: ", first_name, last_name, "\n", "=" * 36) 

#==================================================================================================

# Create a second object called "user2" that contains different data within the already created "first_name" & "last_name" variables.
user2 = User()
user2.first_name = "Frank"
user2.last_name = "Murphy"

print(first_name, last_name, "\n", "=" * 36)

#==================================================================================================

# Attach additional fields to the objects that aren't strings.
# You cannot call upon data to an object that doesn't exist. 
    # For example: If you were to call upon "user2.age", an error would arise due to there being no data assigned.
user1.age = 37
user2.favorite_book = "2001: A Space Odyseey"

print("user1 age: ", user1.age, "\n", "=" * 36)

#==================================================================================================

# Class Features:
    # Methods: Function inside a class
    # Initialization: Function is called everytime object is created in class
    # Help text: Docstrings 

class User:
    # init method that is called everytime when reffering to class
    """A member of FriendFace. For now we are 
        only storing their name and brithday. 
        But soon we will store an uncvomfortable amount of user information.
        XD"""
    def __init__(self, full_name, birthday):
        self.full_name = full_name
        self.birthday = birthday    # yyyymmdd

        # Extract first and last names
        name_pieces = self.full_name.split(" ") 
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm =  int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)   # Date of birthday
        age_in_days = (today-dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

# Create "User", call upon "init" method and print data
user = User("Chris Redfield", "19730104")
print(user.full_name)
print(user.birthday)

# Call upon the "age" method within the class 
print(user.age(), "\n", "=" * 36)

# Use the help function to see your class's information
print(help(User))