# Exceptions
# https://docs.python.org/3/library/exceptions.html

# Example 1 - ZeroDivisionError

try:
    x = 1 / 0
except ZeroDivisionError:
    print('You cannot divide by zero')

# Example 2 - NameError

try:
    print(name)
except NameError:
    print('Variable name is not defined')

# Example 3 - TypeError

try:
    x = 1 + '1'
except TypeError:
    print('You cannot add a number to a string')

# Example 4 - ValueError

try:
    x = int('John')
except ValueError:
    print('Invalid value')

# Example 5 - FileNotFoundError

try:
    file = open('file.txt', 'r')
except FileNotFoundError:
    print('File not found')
