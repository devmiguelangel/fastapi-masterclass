# Statements

# if statement
# https://docs.python.org/3/tutorial/controlflow.html#if-statements

# Example 1: If the number is positive, we print an appropriate message

number = 3

if number > 0:
    print(number, "is a positive number.")

# Example 2: If the number is negative, we print an appropriate message

number = -1

if number > 0:
    print(number, "is a positive number.")

# Logical operators
# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# Example 1: Using and operator

number = 100

if number > 0 and number % 2 == 0:
    print(number, "is a positive and even number.")

# Example 2: Using or operator

number = 101

if number > 0 or number % 2 == 0:
    print(number, "is a positive or even number.")

# Example 3: Using not operator

number = 101

if not number % 2 == 0:
    print(number, "is not an even number.")

# while loop
# https://docs.python.org/3/reference/compound_stmts.html#while

# Example 1: Find the sum of all numbers up to 10

n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("The sum is", sum)

# for loop
# https://docs.python.org/3/tutorial/controlflow.html#for-statements

# Example 1: Find the sum of all numbers up to 10

n = 10
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("The sum is", sum)

# Nested loops

# Example 1: Display multiplication table

for i in range(1, 3):
    for j in range(1, 3):
        print(i, 'x', j, '=', i * j)
    print()

# break and continue statements

# Example 1: Use of break statement inside loop

cart = [10, 20, 30, 40, 50]

for item in cart:
    if item > 30:
        break
    print(item)

# Example 2: Use of continue statement inside loop

cart = [10, 20, 30, 40, 50]

for item in cart:
    if item == 30:
        continue
    print(item)
