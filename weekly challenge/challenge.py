# Task 1: Create a list of integers and compute their sum
def task1():
    print("\n--- Task 1: Sum of Integers in a List ---")
    numbers = []
    while True:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    total_sum = sum(numbers)
    print(f"List of integers: {numbers}")
    print(f"Sum of integers: {total_sum}")


# Task 2: Create a tuple of favorite books and print each one
def task2():
    print("\n--- Task 2: Favorite Books ---")
    favorite_books = (
        "The Alchemist",
        "1984",
        "To Kill a Mockingbird",
        "The Great Gatsby",
        "Pride and Prejudice"
    )
    print("My favorite books:")
    for book in favorite_books:
        print(book)


# Task 3: Store person information in a dictionary and print it
def task3():
    print("\n--- Task 3: Person Information ---")
    person = {}
    person["name"] = input("Enter your name: ")
    person["age"] = int(input("Enter your age: "))
    person["favorite_color"] = input("Enter your favorite color: ")
    
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")


# Task 4: Create two sets of integers and find their common elements
def task4():
    print("\n--- Task 4: Common Elements in Two Sets ---")
    set1 = set()
    set2 = set()
    
    print("Enter integers for the first set (type 'done' to finish):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            set1.add(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print("Enter integers for the second set (type 'done' to finish):")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            set2.add(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    common_elements = set1.intersection(set2)
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Common Elements: {common_elements}")


# Task 5: Filter words with odd number of characters using list comprehension
def task5():
    print("\n--- Task 5: Words with Odd Number of Characters ---")
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    print("Original List of Words:", words)
    
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print("Words with Odd Number of Characters:", odd_length_words)


# Main program
def main():
    print("🌟 Python Tasks Program 🌟")
    task1()  # Task 1: Sum of integers in a list
    task2()  # Task 2: Favorite books tuple
    task3()  # Task 3: Person information dictionary
    task4()  # Task 4: Common elements in two sets
    task5()  # Task 5: Words with odd number of characters


# Run the program
if __name__ == "__main__":
    main()