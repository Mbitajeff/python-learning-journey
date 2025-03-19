def sum_of_integers():
    # Accept user input to create a list of integers
    numbers = input("Enter a list of integers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  # Convert input strings to integers

    # Compute the sum of all integers in the list
    total_sum = sum(numbers)

    # Print the sum
    print("The sum of the integers is:", total_sum)


def favorite_books():
    # Create a tuple of favorite books
    favorite_books = ("To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "The Catcher in the Rye")

    # Use a for loop to print each book name on a separate line
    print("Favorite Books:")
    for book in favorite_books:
        print(book)


def person_information():
    # Create an empty dictionary to store person information
    person_info = {}

    # Ask the user for input and store the information in the dictionary
    person_info["name"] = input("Enter your name: ")
    person_info["age"] = int(input("Enter your age: "))
    person_info["favorite_color"] = input("Enter your favorite color: ")

    # Print the dictionary to the console
    print("Person Information:", person_info)


def common_elements_in_sets():
    # Accept user input to create two sets of integers
    set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
    set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

    # Create a new set containing common elements
    common_elements = set1.intersection(set2)

    # Print the common elements
    print("Common elements in both sets:", common_elements)


def odd_length_words():
    # Store a list of words
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # Use list comprehension to create a new list with words of odd lengths
    odd_length_words = [word for word in words if len(word) % 2 != 0]

    # Print the new list
    print("Words with odd number of characters:", odd_length_words)


def main():
    print("--- Program 1: Sum of Integers ---")
    sum_of_integers()

    print("\n--- Program 2: Favorite Books ---")
    favorite_books()

    print("\n--- Program 3: Person Information ---")
    person_information()

    print("\n--- Program 4: Common Elements in Sets ---")
    common_elements_in_sets()

    print("\n--- Program 5: Words with Odd Lengths ---")
    odd_length_words()


if __name__ == "__main__":
    main()