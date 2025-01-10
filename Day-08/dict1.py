# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary with specified keys
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': '123 Tech Street'
}

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['Machine Learning', 'Cloud Computing'])
print("Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys = list(student.keys())
print("Keys:", keys)

# 8. Get the dictionary values as a list
values = list(student.values())
print("Values:", values)

# 9. Change the dictionary to a list of tuples using the _items() method
items = list(student.items())
print("Items as tuples:", items)

# 10. Delete one of the items in the dictionary
del student['address']
print("Student dictionary after deleting 'address':", student)
