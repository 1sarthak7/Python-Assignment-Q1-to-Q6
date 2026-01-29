#write a python program to perform varios operations on sets:

# 1. Create and access set elements:

my_set = {1, 2, 3, 4, 5}
print("Set elements:", my_set)

# 2. union and intersection of sets:

first_set = {4, 5, 6, 7, 8}

union_set = my_set.union(first_set)          # Union of sets
print("Union of sets:", union_set)

intersection_set = my_set.intersection(first_set)  # Intersection of sets
print("Intersection of sets:", intersection_set)

# 3. Add and Remove elements from a set:

my_set.add(6)                                 # Adding an element
print("After adding an element:", my_set)

my_set.remove(2)                              # Removing an element
print("After removing an element:", my_set)
