# Day 13 Exercises

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("Negative and Zero:", negative_and_zero)


# 2. Flatten the following list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print("Flattened List:", flattened_list)


# 3. Using list comprehension create the following list of tuples
tuple_list = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of Tuples:")
for item in tuple_list:
    print(item)


# 4. Flatten the following list to a new list with country names, country code, and city names in uppercase
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), city.upper()] for [(country, city)] in countries]
print("Flattened Countries:", flattened_countries)


# 5. Change the following list to a list of dictionaries with 'country' and 'city' as keys
country_dicts = [{'country': country[0].upper(), 'city': city.upper()} for [(country, city)] in countries]
print("List of Dictionaries:")
for item in country_dicts:
    print(item)


# 6. Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for [(name)] in names]
print("Concatenated Names:", concatenated_names)


# 7. Lambda function to solve the slope (m) and y-intercept (b) of linear functions
slope_intercept = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1)

# Example use case
m, b = slope_intercept(1, 2, 3, 4)
print(f"Slope: {m}, Y-intercept: {b}")
