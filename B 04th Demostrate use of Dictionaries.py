
# Define a dictionary
my_dict = {'name': 'Srikanth', 'age': 40, 'city': 'Bangalore'}
print("Initial dictionary:", my_dict)

# Access dictionary elements by key
print("Value for 'name':", my_dict['name'])
print("Value for 'age':", my_dict['age'])

# Get value with get method
print("Value for 'country':", my_dict.get('country'))

# Get value with get method which provides a default value if the key is not in the dictionary
print("Value for 'country' with default:", my_dict.get('country', 'India'))

# Change the value of a dictionary item
my_dict['age'] = 35
print("Dictionary after modifying an item:", my_dict)

# Add an item to the dictionary
my_dict['job'] = 'Engineer'
print("Dictionary after adding an item:", my_dict)

# Remove an item from the dictionary by key
del my_dict['city']
print("Dictionary after deleting an item by key:", my_dict)

# Remove an item using pop method
print("Popped item:", my_dict.pop('job'))
print("Dictionary after popping an item:", my_dict)

# Get all keys, values, and items
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))

# Get the number of items in the dictionary
print("Number of items:", len(my_dict))

# Check if a key exists in the dictionary
print("'name' in dictionary:", 'name' in my_dict)
print("'city' in dictionary:", 'city' in my_dict)

# Merge two dictionaries
my_dict2 = {'country': 'India', 'job': 'Engineer'}
my_dict.update(my_dict2)
print("Dictionary after merging:", my_dict)

# Remove all items from the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)
