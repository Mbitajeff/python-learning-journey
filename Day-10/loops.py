# 1. Iterate 0 to 10 using for loop, do the same using while loop.

# For loop
for i in range(11):
    print(i)

print("\n")

# While loop
i = 0
while i <= 10:
    print(i)
    i += 1

print("\n")

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

# For loop
for i in range(10, -1, -1):
    print(i)

print("\n")

# While loop
i = 10
while i >= 0:
    print(i)
    i -= 1

print("\n")

# 3. Write a loop that makes seven calls to print(), so we get the following triangle:

for i in range(1, 8):
    print('#' * i)

print("\n")

# 4. Use nested loops to create the following pattern:

for i in range(8):
    print('# ' * 8)

print("\n")

# 5. Print the following multiplication pattern:

for i in range(11):
    print(f"{i} x {i} = {i * i}")

print("\n")

# 6. Iterate through the list ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using for loop and print out the items.

languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

print("\n")

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(101):
    if i % 2 == 0:
        print(i)

print("\n")

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(101):
    if i % 2 != 0:
        print(i)

print("\n")

# Level 2 Exercises:

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers

total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}.")

print("\n")

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds

even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
