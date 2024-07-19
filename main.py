# This is a program to add, subtract, multiply and divide two numbers

# Part 1: Add and Subtract two numbers
print('This program will add and subtract two numbers')
print()

# Ask user for two different numbers
num_1 = int(input('Please enter the first number:\n'))
num_2 = int(input('Please enter the second number:\n'))
print()

# Tell users what numbers they entered
print('You entered', num_1, 'and', num_2, '\n')

# Add numbers (Result is num_3)
num_3 = num_1 + num_2
print(num_1, '+', num_2, 'is equal to', num_3)

# Subtract numbers (Result is num_4)
num_4 = num_1 - num_2
print(num_1, '-', num_2, 'is equal to', num_4)
print()

# Part2: Multiply and Divide two numbers
print('Now we will multiply and divide two numbers')
print()
# Ask user for two different numbers
num_1 = int(input('Please enter the first number:\n'))
num_2 = int(input('Please enter the second number:\n'))
print()
# Tell users what numbers they entered
print('You entered', num_1, 'and', num_2, '\n')

# Multiply numbers (Result is num_5)
num_5 = num_1 * num_2
print(num_1, '*', num_2, 'is equal to', num_5)

# Divide numbers (result is num_6)
num_6 = num_1 / num_2
print(num_1, '/', num_2, 'is equal to', num_6)
