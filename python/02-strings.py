# Strings and String methods

# Strings are sequences of characters, using the syntax of either single quotes or double quotes

# Single word
name = 'John Doe'
print('name:', name)

# Entire phrase
phrase = "I'm a Python Developer"
print('phrase:', phrase)

# Multi-line string
multi_line = '''Hello,
I am a Python Developer
'''
print('multi_line:', multi_line)

# Strings are arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Get the character at position 1 (remember that the first character has the position 0)
print('name[0]:', name[0])

# Substring. Get the characters from position 2 to position 5 (not included)
print('name[2:5]:', name[2:5])

# The strip() method removes any whitespace from the beginning or the end

# Strip whitespace
print('name.strip():', name.strip())

# The len() method returns the length of a string
print('len(name):', len(name))

# The lower() method returns the string in lower case
print('name.lower():', name.lower())

# The capitalize() method returns the string with the first character capitalized
print('name.capitalize():', name.capitalize())

# The upper() method returns the string in upper case
print('name.upper():', name.upper())

# The replace() method replaces a string with another string
print('name.replace("John", "Jane"):', name.replace('John', 'Jane'))

# The split() method splits the string into substrings if it finds instances of the separator
print('name.split(" "):', name.split(' '))

# The count() method returns the number of times a specified value appears in the string
print('name.count("o"):', name.count('o'))

# The isdigit() method returns True if all the characters are digits, otherwise False
print('name.isdigit():', name.isdigit()) # False

# The isalpha() method returns True if all the characters are alphabets, otherwise False
print('name.isalpha():', name.isalpha()) # False

# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9), otherwise False
print('name.isalnum():', name.isalnum()) # False

# Check if a string is in the string
print('John' in name) # True

# The format() method formats the specified value(s) and insert them inside the string's placeholder
txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49))

# F-strings
# Python f-strings provide a way to embed expressions inside string literals, using curly braces {}.

name = 'John'
age = 36
print(f'His name is {name}. He is {age} years old.')
print(f'His name is {0}. He is {1} years old.'.format(name, age))
print(f'His name is {name}. He is {age} years old.'.upper())
