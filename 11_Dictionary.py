# Dictionaries are also called "Maps"

# Lets assume we make a social media site called "Friendface" and 
# data needs to be saved from user.
# Using dictionaires, we can save all the data into a single object.

# user_id = 209
# message = "D5 E5 C5 C4 G4"
# language = "English"
# datetime = "20230215T12431Z"
# location = (44.590533, -104.715556)

# To create a dictionary, use the curly braces "{}" 
# Enter the value name, then the value "{"value_name" : value}"

# Creates a dictionary with all the values listed above.
# 5 inputs (keys) and 5 outputs (values)
post = {"user_id" : 209, "message" : "D5 E5 C5 C4 G4", "language" : "English", "datetime" : "20230215T12431Z", "location" : (44.590533, -104.715556)}
print("Post 1: ", post, "\n")

# Use dict constructor to create another dictionary
post2 = dict(messages="SS Cotopaxi", language="English")    # NOTICE within costructor, you DO NOT need to use quotes around the keyname.
print("Post 2: ", post2) 

# Add data to post2 dictionary using brackets "[]"
post2["user_id"] = 201  # NOTICE when you use brackets "[]", you DO need to use quotes around the keyname
post2["datetime"] = "2030485842092ZI3"
print("Post 2 update: ", post2, "\n")

# Accessing data in dictionary
print("Post 2 message data: ", post2["messages"], "\n")

# You can only access data within the dictionary. If a keyname is not populated with a value you can:
# Use "in" operator to check if key is in dictionary.
if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value.", "\n")

# Iterate over all key value pairs in the dictionary "post"
print("Iterating over all keys in dictionary: ")
print("---------------------------------------")
for key in post.keys(): # The keys method gives object that we can loop over all keys in dictionary.
    value = post[key]
    print(key, "=", value)
print("\n")

# Iterate over all keys pairs in dictionary "post" using "items" dict.method.
# This method gives the key and values throughout each iteration
print("Iterating over all keys in dictionary using 'dict.items' method: ")
print("-----------------------------------------------------------------")
for key, value in post.items(): # Translation: "For "key" & "value" in dictionary post using "dict.items" method,
    print(key, "=", value)      # Print the "key", "=" string, and "value" to the console
print("\n")

# Remove elements from dictionary "post" using "dict.pop" method then iterate over all key pairs using "dict.items" method.
print("Removing elements from dictionary post using pop method")
print("-------------------------------------------------------")
post.pop("user_id")
for key, value in post.items(): 
    print(key, "=", value)      
print("\n")

# Remove all elements from dictionary "post" using "dict.clear" method
print("Removing ALL elements from dictionary post using clear method")
print("-------------------------------------------------------------")
post.clear()
for key, value in post.items(): 
    print(key, "=", value)      
print("\n")
