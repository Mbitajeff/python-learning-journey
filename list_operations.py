# Step 1: Create an empty list called my_list
my_list = []
print("Step 1: Empty list created:", my_list)

# Step 2: Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2: After appending elements:", my_list)

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position
print("Step 3: After inserting 15 at the second position:", my_list)

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("Step 4: After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element from my_list
my_list.pop()  # Removes the last element by default
print("Step 5: After removing the last element:", my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()
print("Step 6: After sorting in ascending order:", my_list)

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Step 7: Index of the value 30:", index_of_30)