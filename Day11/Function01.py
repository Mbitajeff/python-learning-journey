import math
import cmath

# 1. Add Two Numbers
def add_two_numbers(a, b):
    return a + b

# 2. Area of a Circle
def area_of_circle(r):
    return math.pi * r ** 2

# 3. Add All Numbers
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All items must be numbers."

# 4. Convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5. Check Season
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    return 'Invalid month'

# 6. Calculate Slope
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    return (y2 - y1) / (x2 - x1)

# 7. Solve Quadratic Equation
def solve_quadratic_eqn(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

# 8. Print List
def print_list(lst):
    for item in lst:
        print(item)

# 9. Reverse List
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 10. Capitalize List Items
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Add Item
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Remove Item
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Sum of Numbers
def sum_of_numbers(n):
    return sum(range(n + 1))

# 14. Sum of Odds
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15. Sum of Even
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Test the functions
if __name__ == "__main__":
    # Testing examples
    print(add_two_numbers(3, 5))
    print(area_of_circle(7))
    print(add_all_nums(1, 2, 3, 'a'))  # Will return error message
    print(convert_celsius_to_fahrenheit(0))
    print(check_season("June"))
    print(calculate_slope(2, 3, 5, 7))
    print(solve_quadratic_eqn(1, -3, 2))
    print_list([1, 2, 3, 4, 5])
    print(reverse_list([1, 2, 3, 4, 5]))
    print(capitalize_list_items(["apple", "banana", "cherry"]))
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(add_item(food_staff, 'Meat'))
    print(remove_item(food_staff, 'Mango'))
    print(sum_of_numbers(10))
    print(sum_of_odds(10))
    print(sum_of_even(10))
