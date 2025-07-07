# Creating a list
my_list = [1, 2, 3, "apple", "banana"]
print(f"Original list: {my_list}")

# Accessing elements (indexing)
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")

# Slicing a list
print(f"Slice from index 1 to 3 (exclusive): {my_list[1:4]}")

# Modifying elements
my_list[0] = 10
print(f"List after modifying first element: {my_list}")

# Adding elements
my_list.append("cherry") # Add to the end
print(f"List after appending 'cherry': {my_list}")
my_list.insert(1, "orange") # Insert at a specific index
print(f"List after inserting 'orange' at index 1: {my_list}")

# Removing elements
my_list.remove("banana") # Remove by value
print(f"List after removing 'banana': {my_list}")
popped_item = my_list.pop() # Remove and return the last element
print(f"List after popping last element: {my_list}, Popped item: {popped_item}")
del my_list[0] # Delete by index
print(f"List after deleting element at index 0: {my_list}")

# List length
print(f"Length of the list: {len(my_list)}")

# Checking if an item exists
print(f"Is 'apple' in the list? {'apple' in my_list}")

# Iterating through a list
print("Iterating through the list:")
for item in my_list:
    print(item)


# Creating a tuple
my_tuple = (1, 2, "apple", "banana")
print(f"Original tuple: {my_tuple}")

# Accessing elements (indexing)
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")

# Slicing a tuple
print(f"Slice from index 1 to 3 (exclusive): {my_tuple[1:4]}")

# Attempting to modify (will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error trying to modify a tuple: {e}")

# Tuple length
print(f"Length of the tuple: {len(my_tuple)}")

# Concatenating tuples
another_tuple = ("cherry", "date")
combined_tuple = my_tuple + another_tuple
print(f"Combined tuple: {combined_tuple}")

# Iterating through a tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)


# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Original dictionary: {my_dict}")

# Accessing values by key
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict.get('age')}") # Using .get() is safer as it returns None if key not found

# Modifying values
my_dict["age"] = 31
print(f"Dictionary after modifying age: {my_dict}")

# Adding new key-value pairs
my_dict["occupation"] = "Engineer"
print(f"Dictionary after adding occupation: {my_dict}")

# Removing key-value pairs
removed_value = my_dict.pop("city") # Remove and return value for a key
print(f"Dictionary after removing city: {my_dict}, Removed value: {removed_value}")
del my_dict["name"] # Delete by key
print(f"Dictionary after deleting name: {my_dict}")

# Dictionary length
print(f"Length of the dictionary: {len(my_dict)}")

# Getting all keys, values, and items
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items (key-value pairs): {my_dict.items()}")

# Iterating through a dictionary
print("Iterating through dictionary keys:")
for key in my_dict:
    print(key)

print("Iterating through dictionary values:")
for value in my_dict.values():
    print(value)

print("Iterating through dictionary items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Creating a set
my_set = {1, 2, 3, 2, 4, 1} # Duplicates are automatically removed
print(f"Original set: {my_set}")

# Adding elements
my_set.add(5)
print(f"Set after adding 5: {my_set}")
my_set.update([6, 7, 1]) # Add multiple elements
print(f"Set after updating with [6, 7, 1]: {my_set}")

# Removing elements
my_set.remove(3) # Raises an error if item not found
print(f"Set after removing 3: {my_set}")
my_set.discard(10) # Does not raise an error if item not found
print(f"Set after discarding 10: {my_set}")
popped_item = my_set.pop() # Remove and return an arbitrary element
print(f"Set after popping an element: {my_set}, Popped item: {popped_item}")

# Set length
print(f"Length of the set: {len(my_set)}")

# Checking for membership
print(f"Is 4 in the set? {4 in my_set}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

print(f"Union (all unique elements): {set_a.union(set_b)}")
print(f"Intersection (common elements): {set_a.intersection(set_b)}")
print(f"Difference (elements in A but not in B): {set_a.difference(set_b)}")
print(f"Symmetric difference (elements in either A or B, but not both): {set_a.symmetric_difference(set_b)}")

# Iterating through a set
print("Iterating through the set:")
for item in my_set:
    print(item)