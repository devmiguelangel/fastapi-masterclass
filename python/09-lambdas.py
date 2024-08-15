# Walrus operator
# Python 3.8 introduced the walrus operator (:=), which allows you to assign values to variables as part of an expression.
# The walrus operator is useful for simplifying code and improving readability, especially when working with while loops and list comprehensions.

print('#########################')
print('Walrus operator')
print('#########################')

# Example 1: While Loop
# The walrus operator can be used to assign a value to a variable inside a while loop condition.
# This allows you to avoid repeating the assignment statement inside the loop body.

# Without walrus operator
fruits = ['apple', 'banana', 'cherry']
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# With walrus operator
fruits = ['apple', 'banana', 'cherry']
i = 0

while (n := len(fruits)) > i:
    print(fruits[i])
    i += 1

# Lambda Functions
# Lambda functions are anonymous functions that can be defined using the lambda keyword.
# They are useful for creating small, simple functions that are used only once.
# Lambda functions can take any number of arguments, but can only have one expression.
# The result of the expression is automatically returned by the lambda function.

print('#########################')
print('Lambda Functions')
print('#########################')

# Example 1: Simple Lambda Function
# This lambda function takes two arguments x and y, and returns their sum.
add = lambda x, y: x + y
print('add(2, 3):', add(2, 3))

# Example 2: Using Lambda Function with Built-in Functions
# You can use lambda functions with built-in functions like map(), filter(), and reduce().
# The map() function applies a function to each item in an iterable.
# The filter() function filters items in an iterable based on a condition.
# The reduce() function applies a function to an iterable and returns a single value.

# Using map() with lambda function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print('squared:', squared)

# Using filter() with lambda function
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print('even:', even)

# Using reduce() with lambda function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print('total:', total)

# Example 3: Using Lambda Function with User-defined Functions
# You can also use lambda functions with user-defined functions.
# This example defines a function that takes a lambda function as an argument and calls it with the given arguments.

def apply(func, x, y):
    return func(x, y)

result = apply(lambda x, y: x * y, 2, 3)
print('result:', result)

# Example 4: Using Lambda Function with List Comprehension
# You can use lambda functions with list comprehension to create new lists based on existing lists.
# This example creates a list of squares using a lambda function and list comprehension.

numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x ** 2)(x) for x in numbers]
print('squared:', squared)


# Example 5: Using Lambda Function with Sorting
# You can use lambda functions to define custom sorting criteria for the sorted() function.
# This example sorts a list of tuples based on the second element of each tuple.

students = [
    ('Alice', 'F', 25),
    ('Bob', 'M', 20),
    ('Charlie', 'M', 30),
    ('David', 'M', 22),
]

sorted_students = sorted(students, key=lambda x: x[2], reverse=True)

print('sorted fn:')
for student in sorted_students:
    print(student)

# Example 6: Using Lambda Function with Map and Filter

# Map
# This example uses a lambda function with map() to convert a list of strings to uppercase.

store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('shoes', 50.00),
]

to_euros = lambda x: (x[0], x[1] * 0.85)

store_euros = list(map(to_euros, store))

print('map fn:')

for item in store_euros:
    print(item)

# Filter
# This example uses a lambda function with filter() to filter out items that are less than 30.00.

store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('shoes', 50.00),
]

expensive = list(filter(lambda x: x[1] > 30.00, store))

print('filter fn:')

for item in expensive:
    print(item)
