# Finding lengths
len_python = len("python")
len_dragon = len("dragon")

# Falsy comparison statement
falsy_comparison = len_python > len_dragon  # This is False because both lengths are 6

print(f"Length of 'python': {len_python}")
print(f"Length of 'dragon': {len_dragon}")
print(f"Falsy comparison (len_python > len_dragon): {falsy_comparison}")

# Dragon
# Checking 'on' in both words
has_on = 'on' in 'python' and 'on' in 'dragon'
print(f"'on' found in both 'python' and 'dragon': {has_on}")

# Check if jargon is in the sentence
sentence = "I hope this course is not full of jargon"
has_jargon = "jargon" in sentence
print(f"'jargon' is in the sentence: {has_jargon}")

#Script to calculate pay based on hours and rate
# Prompt user for hours and rate
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

# Calculate pay
weekly_earning = hours * rate
print(f"Your weekly earning is {weekly_earning}")
