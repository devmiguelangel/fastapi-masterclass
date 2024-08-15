# Lists
# https://docs.python.org/3/library/stdtypes.html#list
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# Example 1: Create a list

print('#########################')
print('LISTS')
print('#########################')

fruits = ['apple', 'banana', 'cherry', 'blueberry', 'kiwi', 'mango']

print(type(fruits), fruits)

# Example 2: Access items

print('fruits[2]:', fruits[2])

# Example 3: Change item value

fruits[2] = 'orange'

print('fruits[2]:', fruits[2])

# Example 4: Loop through a list

for fruit in fruits:
    print(fruit)

# Example 5: Check if item exists

if 'apple' in fruits:
    print('Yes, apple is in the fruits list')

# Example 6: Methods

# append()	Adds an element at the end of the list
fruits.append('pear')
# remove()	Removes the first item with the specified value
fruits.remove('blueberry')
# pop()	Removes the element at the specified position
fruits.pop(1)
# insert()	Adds an element at the specified position
fruits.insert(1, 'banana')
# copy()	Returns a copy of the list
fruits_copy = fruits.copy()
# sort()	Sorts the list
fruits.sort()
# clear()	Removes all the elements from the list
fruits.clear()
# count()	Returns the number of elements with the specified value

print('fruits:', fruits, fruits_copy)

# 2d lists

drinks = ['coffee', 'tea', 'milk']
dinner = ['pizza', 'burger', 'hotdog']
dessert = ['cake', 'ice cream']

print('2D LISTS', [drinks, dinner, dessert])

# Tuples
# https://docs.python.org/3/library/stdtypes.html#tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

print('#########################')
print('TUPLES')
print('#########################')

# Example 1: Create a tuple

fruits = ('apple', 'banana', 'cherry', 'blueberry', 'kiwi', 'mango')

print(type(fruits), fruits)

# Example 2: Access items

print('fruits[2]:', fruits[2])

# Example 3: Count items

print('fruits.count("apple"):', fruits.count('apple'))

# Sets
# https://docs.python.org/3/library/stdtypes.html#set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

print('#########################')
print('SETS')
print('#########################')

# Example 1: Create a set

fruits = {'apple', 'banana', 'cherry', 'blueberry', 'kiwi', 'mango'}

print(type(fruits), fruits)

# Example 2: Add items

fruits.add('orange')
print('fruits:', fruits)

# Example 3: Remove items

fruits.remove('blueberry')
print('fruits:', fruits)

# Example 4: Loop through a set

for fruit in fruits:
    print(fruit)


# Dictionaries
# https://docs.python.org/3/library/stdtypes.html#dict
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

print('#########################')
print('DICTIONARIES')
print('#########################')

# Example 1: Create a dictionary

capitals = {
    'USA': 'Washington D.C.',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'UK': 'London',
}

print(type(capitals), capitals)

# Example 2: Access items

print('capitals["USA"]:', capitals.get('USA'))

# Example 3: loop through a dictionary

for country, capital in capitals.items():
    print(country, capital)

# Example 4: Get keys

print('capitals.keys():', capitals.keys())

# Example 5: Get values

print('capitals.values():', capitals.values())

# Example 6: Get items

print('capitals.items():', capitals.items())


# Example 7: List Comprehensions
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

print('#########################')
print('LIST COMPREHENSIONS')
print('#########################')

numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print('squared:', squared)


# Example 8: Dictionary Comprehensions

print('#########################')
print('DICTIONARY COMPREHENSIONS')
print('#########################')

capitals = {
    'USA': 'Washington D.C.',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'UK': 'London',
}

capitals_upper = {country: capital.upper() for country, capital in capitals.items()}
print('capitals_upper:', capitals_upper)

# Example 9: Zip Function
# https://docs.python.org/3/library/functions.html#zip

# The zip() function returns an iterator of tuples based on the iterable objects.
# If the input iterables are of different lengths, the resulting iterator stops when the shortest input iterable is exhausted.

print('#########################')
print('ZIP FUNCTION')
print('#########################')

countries = ['USA', 'France', 'Germany', 'Italy', 'Spain', 'UK']
capitals = ['Washington D.C.', 'Paris', 'Berlin', 'Rome', 'Madrid', 'London']

countries_capitals = dict(zip(countries, capitals))

print('countries_capitals:', countries_capitals)
