# Define a tuple for a student
student = ("John Doe", 20, "Computer Science", 3.5)

# Accessing tuple elements
name = student[0]
age = student[1]
major = student[2]
gpa = student[3]

# Print student information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"GPA: {gpa}")

# Creating a tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Accessing elements
x, y = coordinates
print("X:", x, "Y:", y)

# Tuples are immutable (uncommenting the line below will raise an error)
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print("2")