# Exercises: Level 1

# 1. Check if the user is old enough to drive
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare my_age and your_age
my_age = 25  # Replace with your age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} {'year' if diff == 1 else 'years'} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} {'year' if diff == 1 else 'years'} older than you.")
else:
    print("We are the same age!")

# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2

# 1. Assign grades based on scores
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("Invalid score.")

# 2. Check the season
month = input("Enter the month: ").strip().lower()

if month in ['september', 'october', 'november']:
    print("The season is Autumn.")
elif month in ['december', 'january', 'february']:
    print("The season is Winter.")
elif month in ['march', 'april', 'may']:
    print("The season is Spring.")
elif month in ['june', 'july', 'august']:
    print("The season is Summer.")
else:
    print("Invalid month.")

# 3. Add fruit to the list or check if it exists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Updated fruit list:", fruits)

# Exercises: Level 3

# 1. Manipulate the person dictionary
person = {
    'first_name': 'Jeff',
    'last_name': 'Mbita',
    'age': 250,
    'country': 'Nairobi',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Tom Mboya Street',
        'zipcode': '02210'
    }
}

# Check if the person has multiple skills
if len(person['skills']) > 1:
    print(f"{person['first_name']} has multiple skills: {', '.join(person['skills'])}")

# Check if 'Python' is in the skills list
if 'Python' in person['skills']:
    print("Python is one of their skills.")

# Add a new skill
person['skills'].append('AWS')
print("Updated skills:", person['skills'])

# Access the person's address
print("Address:", person['address']['street'], person['address']['zipcode'])

if __name__ == "__main__" : 

    num1 = 15 
    num2 = 12 

sum_twoNum = lambda num1, num2 : num1 + num2 

print("Sum of {0} and {1} is {2};" .format(num1, num2, sum_twoNum(num1, num2))) 
