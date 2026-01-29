#Write a Python program to perform following operations on Dictionaries:

# 1. Create and access dictionary elements:
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary elements:", my_dict)

# Accessing elements
print("Value for key 'a':", my_dict['a'])
print("Value for key 'c':", my_dict.get('c'))

# 2. Add and Remove elements from a dictionary:
my_dict['d'] = 4                          # Adding an element
print("After adding an element:", my_dict)
del my_dict['b']                          # Removing an element
print("After removing an element:", my_dict)

# 3. update dictionary:
my_dict.update({'c': 30, 'e': 5})
print("After updating the dictionary:", my_dict)

# 4. merging dictionaries:
another_dict = {'f': 6, 'g': 7}
merged_dict = {**my_dict, **another_dict}
print("Merged dictionary:", merged_dict)
