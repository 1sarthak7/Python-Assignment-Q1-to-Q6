# write a python program to perform various operations on tuples

# 1. Create and access tuple elements:

# Creating a tuple
my_tuple = (100, 200, 300, 400, 500)
print("Tuple elements:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 2. Concatenate and Repeat tuples:

# Creating next tuple
another_tuple = (600, 700, 800)

# Concatenating tuple
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repeating tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# 3. Slicing and Unpacking tuple:

# Slicing the tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)

# nesteed tuple
nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)


