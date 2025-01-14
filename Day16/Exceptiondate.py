# Demonstrating exception handling
def handle_exceptions():
    try:
        name = input('Enter your name: ')
        year_born = int(input('Year you were born: '))
        age = 2019 - year_born
        print(f'You are {name}. And your age is {age}.')
    except TypeError:
        print('Type error occurred')
    except ValueError:
        print('Value error occurred')
    except ZeroDivisionError:
        print('Zero division error occurred')
    else:
        print('I usually run with the try block')
    finally:
        print('I always run.')

# Packing and Unpacking arguments (lists and dictionaries)
def packing_unpacking():
    # Unpacking lists
    lst = [1, 2, 3, 4, 5]
    a, b, c, d, e = lst
    print(f'Unpacked list: {a}, {b}, {c}, {d}, {e}')

    # Unpacking dictionaries
    def unpacking_person_info(name, country, city, age):
        return f'{name} lives in {country}, {city}. He is {age} years old.'
    
    dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
    print(unpacking_person_info(**dct))

    # Packing arguments
    def sum_all(*args):
        return sum(args)
    
    print(f'Sum of all numbers: {sum_all(1, 2, 3, 4)}')

    # Packing dictionaries
    def packing_person_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250)

# Spreading in Python
def spreading_example():
    lst_one = [1, 2, 3]
    lst_two = [4, 5, 6, 7]
    combined_lst = [0, *lst_one, *lst_two]
    print(f'Combined List: {combined_lst}')
    
    countries_one = ['Finland', 'Sweden', 'Norway']
    countries_two = ['Denmark', 'Iceland']
    nordic_countries = [*countries_one, *countries_two]
    print(f'Nordic Countries: {nordic_countries}')

# Enumerate function example
def enumerate_example():
    countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
    for index, country in enumerate(countries):
        print(f'{index}: {country}')

# Zip function example
def zip_example():
    fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    
    fruits_and_veges = []
    for f, v in zip(fruits, vegetables):
        fruits_and_veges.append({'fruit': f, 'veg': v})
    
    print(f'Fruits and Vegetables: {fruits_and_veges}')

# Unpacking and splitting a list
def unpack_split_list():
    names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
    
    nordic_countries, es, ru = names[:5], names[5], names[6]
    print(f"Nordic countries: {nordic_countries}")
    print(f"Estonia: {es}")
    print(f"Russia: {ru}")

# Running all the examples
def run_all_examples():
    print("=== Handling Exceptions ===")
    handle_exceptions()
    
    print("\n=== Packing and Unpacking Arguments ===")
    packing_unpacking()
    
    print("\n=== Spreading in Python ===")
    spreading_example()
    
    print("\n=== Enumerate Function Example ===")
    enumerate_example()
    
    print("\n=== Zip Function Example ===")
    zip_example()
    
    print("\n=== Unpacking and Splitting List Example ===")
    unpack_split_list()

# Run the summary of all topics
run_all_examples()
