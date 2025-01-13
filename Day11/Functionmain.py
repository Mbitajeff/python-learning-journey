import math
from statistics import mean, median, mode, variance, stdev

# Level 2

# 1. Evens and Odds
def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}. The number of evens are {evens}."

# 2. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 3. Check if Empty
def is_empty(value):
    if value == "" or value is None:
        return True
    return False

# 4. List Statistics

# Mean
def calculate_mean(lst):
    return mean(lst)

# Median
def calculate_median(lst):
    return median(lst)

# Mode
def calculate_mode(lst):
    try:
        return mode(lst)
    except:
        return "No mode found (all values are unique)."

# Range
def calculate_range(lst):
    return max(lst) - min(lst)

# Variance
def calculate_variance(lst):
    return variance(lst)

# Standard Deviation
def calculate_std(lst):
    return stdev(lst)

# Level 3

# 1. Check if Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2. Check if All Items are Unique
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Check if All Items are the Same Data Type
def all_same_data_type(lst):
    if len(lst) == 0:
        return True
    first_type = type(lst[0])
    return all(isinstance(i, first_type) for i in lst)

# 4. Check if Valid Python Variable
def is_valid_python_variable(variable_name):
    if variable_name.isidentifier() and not variable_name[0].isdigit():
        return True
    return False

# 5. Most Spoken Languages and Most Populated Countries (Sample Data)

# Assume we have a `countries-data.py` containing a dictionary of country data:
# Example:
# countries_data = {
#     'China': {'language': 'Mandarin', 'population': 1393409038},
#     'India': {'language': 'Hindi', 'population': 1366417754},
#     'United States': {'language': 'English', 'population': 329484123},
#     # Add more countries as needed
# }

# We simulate the data in this example.
countries_data = {
    'China': {'language': 'Mandarin', 'population': 1393409038},
    'India': {'language': 'Hindi', 'population': 1366417754},
    'United States': {'language': 'English', 'population': 329484123},
    'Indonesia': {'language': 'Indonesian', 'population': 270625568},
    'Pakistan': {'language': 'Urdu', 'population': 220892340},
    'Brazil': {'language': 'Portuguese', 'population': 211049527},
    'Nigeria': {'language': 'English', 'population': 206139589},
    'Bangladesh': {'language': 'Bengali', 'population': 164689383},
    'Russia': {'language': 'Russian', 'population': 145934462},
    'Mexico': {'language': 'Spanish', 'population': 128933395},
}

# Function to get most spoken languages
def most_spoken_languages():
    language_count = {}
    for country, data in countries_data.items():
        language = data['language']
        language_count[language] = language_count.get(language, 0) + 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]

# Function to get most populated countries
def most_populated_countries():
    sorted_countries = sorted(countries_data.items(), key=lambda x: x[1]['population'], reverse=True)
    return [(country, data['population']) for country, data in sorted_countries[:10]]

# Testing Level 2 and Level 3 Functions

if __name__ == "__main__":
    # Testing Level 2 Functions
    print(evens_and_odds(100))
    print(factorial(5))
    print(is_empty(""))
    print(is_empty("Non-empty"))
    print(calculate_mean([1, 2, 3, 4, 5]))
    print(calculate_median([1, 2, 3, 4, 5]))
    print(calculate_mode([1, 1, 2, 3, 4]))
    print(calculate_range([1, 2, 3, 4, 5]))
    print(calculate_variance([1, 2, 3, 4, 5]))
    print(calculate_std([1, 2, 3, 4, 5]))

    # Testing Level 3 Functions
    print(is_prime(7))
    print(all_unique([1, 2, 3, 4, 5]))
    print(all_same_data_type([1, 2, 3, 4, 5]))
    print(is_valid_python_variable("valid_variable"))
    print(is_valid_python_variable("2invalid"))
    
    print("Most Spoken Languages:", most_spoken_languages())
    print("Most Populated Countries:", most_populated_countries())
