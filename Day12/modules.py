import random
import string

# Level 1

# 1. Random User ID Generator (6 characters)
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# 2. User ID Generator by User Input
def user_id_gen_by_user():
    length = int(input("Enter the length of the user ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    user_ids = []
    for _ in range(num_ids):
        user_ids.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    return '\n'.join(user_ids)

# 3. RGB Color Generator
def rgb_color_gen():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

# Level 2

# 1. List of Hexadecimal Colors
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_colors.append(f"#{''.join(random.choices('0123456789ABCDEF', k=6))}")
    return hex_colors

# 2. List of RGB Colors
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        rgb_colors.append(f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})")
    return rgb_colors

# 3. Generate Colors (Hexa or RGB)
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return []

# Level 3

# 1. Shuffle List
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# 2. Generate 7 Unique Random Numbers (Range 0-9)
def unique_random_numbers():
    return random.sample(range(0, 10), 7)

# Testing the functions
if __name__ == "__main__":
    # Level 1
    print("Random User ID:", random_user_id())
    print("User ID Generator by User Input:")
    print(user_id_gen_by_user())
    print("RGB Color Generator:", rgb_color_gen())

    # Level 2
    print("List of Hexadecimal Colors:", list_of_hexa_colors(3))
    print("List of RGB Colors:", list_of_rgb_colors(3))
    print("Generated Colors (Hexa, 3 colors):", generate_colors('hexa', 3))
    print("Generated Colors (RGB, 3 colors):", generate_colors('rgb', 3))

    # Level 3
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Shuffled List:", shuffle_list(sample_list))
    print("Unique Random Numbers (0-9):", unique_random_numbers())
