# Example
Mobile = {"brand": "Samsung", "model": "S10", "Screen Size": 6.1}
print(Mobile)

#Accessing
X = Mobile["model"]
Y = Mobile.get("model")
print(X)
print(Y)

# Modifying / Updating existing value
Mobile["model"] = "S11"
print(Mobile)

# Adding new element
Mobile ["colour"] = "blue"
print(Mobile)

# Deleting
del Mobile["colour"]
print(Mobile)

# Remove last inserted item
Mobile.popitem()

# Looping Through a Dictionary
# Print all keys
for key in Mobile:
    print(key)
# Print all values
for key in Mobile:
    print(Mobile[key])

# Dictionary Functions: dict.values(), dict.items()
# Print all values
for value in Mobile.values():
    print(value)
# Print keys and values
for key, value in Mobile.items():
    print(key, value)

# Checking Key Existence
if "model" in Mobile:
    print("Yes, 'model' is a key in Mobile dictionary")

# Copying a Dictionary
Mobilephone = Mobile.copy()