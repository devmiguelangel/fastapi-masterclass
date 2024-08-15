# Functions
# Functions are a way to group code that belongs together. They are defined using the def keyword.

# Example 1

def greet():
    print('Hello, World!')

greet()

# Example 2 - Arguments

def greet(name):
    print('Hello, ' + name + '!')

greet('John')

# Example 3 - Return Values

def greet(name):
    return 'Hello, ' + name + '! Welcome!'

message = greet('John')
print(message)

# Example 4 - Keyword Arguments. You can also send arguments with the key = value syntax.

def greet(name, age):
    print('Hello, ' + name + '! You are ' + str(age) + ' years old.')

greet(name='John', age=36)

# Example 5 - Nested Functions. A function can call another function.

def greet(name):
    def get_message():
        return 'Hello, '

    result = get_message() + name
    return result

print(greet('John'))

# Example 6 - Variable Scope. Variables defined inside a function are not accessible from outside the function.

def greet(name):
    message = 'Hello, ' + name + '!'
    return message

print(greet('John'))
# print(message) # This will raise an error

# Example 7 - Global Variables. Variables defined outside a function are accessible from inside the function.

message = 'Hello, World!'

def greet(name):
    return message + ' ' + name

print(greet('John'))

# Example 8 - *args. If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def greet(*args):
    for name in args:
        print('Hello, ' + name)

greet('John', 'Jane', 'Jack', 'Jill')

# Example 9 - **kwargs. If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

greet(name='John', age=36, city='New York')
