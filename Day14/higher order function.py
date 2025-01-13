from functools import reduce

# Given lists
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 1 Exercises
# 1. Difference between map, filter, and reduce:
# map: Applies a given function to all items in the input list (or any iterable) and returns a new list with the results.
# filter: Filters out items from the input list (or iterable) based on a condition and returns a new list with the items that satisfy the condition.
# reduce: Applies a given function cumulatively to the items in an iterable and reduces it to a single value (such as summing all numbers).

# 2. Difference between higher-order function, closure, and decorator:
# Higher-order function: A function that takes one or more functions as arguments, or returns a function as a result.
# Closure: A function that remembers and has access to variables from its containing (enclosing) function, even after the enclosing function has finished executing.
# Decorator: A function that takes another function and extends its behavior without explicitly modifying it. It is used to add functionality to an existing function.

# 3. Example of calling function before using map, filter, or reduce
def square(x):
    return x * x

squares = map(square, numbers)
print(list(squares))

# 4. Use for loop to print each country in the countries list
for country in countries:
    print(country)

# 5. Use for loop to print each name in the names list
for name in names:
    print(name)

# 6. Use for loop to print each number in the numbers list
for number in numbers:
    print(number)

# Level 2 Exercises
# 1. Use map to create a new list by changing each country to uppercase in the countries list
uppercased_countries = list(map(lambda country: country.upper(), countries))
print("Uppercased countries:", uppercased_countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda number: number ** 2, numbers))
print("Squared numbers:", squared_numbers)

# 3. Use map to change each name to uppercase in the names list
uppercased_names = list(map(lambda name: name.upper(), names))
print("Uppercased names:", uppercased_names)

# 4. Use filter to filter out countries containing 'land'.
countries_without_land = list(filter(lambda country: 'land' not in country, countries))
print("Countries without 'land':", countries_without_land)

# 5. Use filter to filter out countries having exactly six characters
countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))
print("Countries with exactly six characters:", countries_with_six_chars)

# 6. Use filter to filter out countries containing six letters and more in the country list
countries_with_six_or_more_chars = list(filter(lambda country: len(country) >= 6, countries))
print("Countries with six or more letters:", countries_with_six_or_more_chars)

# 7. Use filter to filter out countries starting with an 'E'
countries_starting_with_e = list(filter(lambda country: country[0] == 'E', countries))
print("Countries starting with 'E':", countries_starting_with_e)

# 8. Chain two or more list iterators (map, filter, reduce)
# Example: Convert names to uppercase and filter those with length greater than 6
result = list(
    filter(lambda name: len(name) > 6, map(lambda name: name.upper(), names))
)
print("Names with more than 6 characters (uppercase):", result)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

string_items = get_string_lists([1, "Hello", 2, "World", 3])
print("String items:", string_items)

# 10. Use reduce to sum all the numbers in the numbers list.
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

# 11. Use reduce to concatenate all the countries and produce this sentence
countries_sentence = reduce(lambda x, y: x + ", " + y, countries) + " are north European countries"
print("Countries sentence:", countries_sentence)
