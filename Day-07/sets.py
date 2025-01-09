# Define initial sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
print(f"Length of it_companies: {len(it_companies)}")

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"After adding 'Twitter': {it_companies}")

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'SAP', 'Dell', 'Adobe'})
print(f"After adding multiple companies: {it_companies}")

# Remove one of the companies from the set it_companies
it_companies.remove('Google')
print(f"After removing 'Google': {it_companies}")

# Difference between remove and discard
# remove raises KeyError if the element is not found, discard does not
it_companies.discard('NonExistentCompany')  # No error
# it_companies.remove('NonExistentCompany')  # Uncommenting this will raise KeyError

# Exercises: Level 2
# Join A and B
union_set = A.union(B)
print(f"A union B: {union_set}")

# Find A intersection B
intersection_set = A.intersection(B)
print(f"A intersection B: {intersection_set}")

# Is A subset of B
print(f"Is A a subset of B? {A.issubset(B)}")

# Are A and B disjoint sets
print(f"Are A and B disjoint sets? {A.isdisjoint(B)}")

# Join A with B and B with A
print(f"A union B: {A.union(B)}")
print(f"B union A: {B.union(A)}")

# Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {symmetric_difference}")

# Delete the sets completely
del A
del B
print("Sets A and B have been deleted.")

# Exercises: Level 3
# Convert age to a set and compare lengths
age_set = set(age)
print(f"Length of age list: {len(age)}")
print(f"Length of age set: {len(age_set)}")
if len(age) > len(age_set):
    print("The list is bigger.")
else:
    print("The set is bigger.")

# Difference between string, list, tuple, and set
print("""
Difference between data types:
- String: Immutable sequence of characters, e.g., 'hello'.
- List: Mutable, ordered collection of items, e.g., [1, 2, 3].
- Tuple: Immutable, ordered collection of items, e.g., (1, 2, 3).
- Set: Unordered, mutable collection of unique items, e.g., {1, 2, 3}.
""")

# Unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")
