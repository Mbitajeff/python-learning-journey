# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)

# Adding elements
unique_numbers.add(6)
print("After Adding 6:", unique_numbers)

# Removing elements
unique_numbers.remove(3)
print("After Removing 3:", unique_numbers)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference (A - B):", set_a - set_b)