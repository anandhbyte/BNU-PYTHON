
# Define the list
my_list = [10, 20, 30, 3.142, 'Python', 'BCA']
print("Initial list:", my_list)

# Access list elements by index
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])

# Change the value of a list item
my_list[4] = 'Java'
print("List after modifying an item:", my_list)

# Add an item to the end of the list and print
my_list.append('Skyward')
print("List after appending an item:", my_list)

# Remove an item from the list by value and print
my_list.remove('Java')
print("List after removing an item:", my_list)

# Remove an item from the list by index and print
del my_list[0]
print("List after deleting an item by index:", my_list)

# Pop an item and print
print("Popped item:", my_list.pop(1))
print("List after popping an item:", my_list)

# Print index of an item directly
print("Index of 'BCA':", my_list.index('BCA'))

# Print count of an item directly
print("Count of 3.142:", my_list.count(3.142))

# Print length of the list directly
print("Length of the list:", len(my_list))

# Reverse a list and print
my_list.reverse()
print("Reversed list:", my_list)

# Clear the list and print
my_list.clear()
print("List after clearing:", my_list)
