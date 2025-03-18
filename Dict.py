# Creating a dictionary
user = {
    "name": "Jeff Mbita",
    "age": 25,
    "occupation": "Cloud Engineer"
}
print("User:", user)

# Accessing values
print("Name:", user["name"])

# Adding a new key-value pair
user["location"] = "Nairobi"
print("After Adding Location:", user)

# Modifying a value
user["age"] = 26
print("After Modifying Age:", user)

# Removing a key-value pair
del user["occupation"]
print("After Removing Occupation:", user)