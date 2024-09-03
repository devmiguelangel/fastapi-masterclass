"""
Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
The child class can use the properties and methods of the parent class as if they were its own.
It can also have additional attributes or methods or override the inherited ones to provide specific behavior.

Step-by-step Example:
1. Define a Parent Class: We'll start by creating a parent class called Employee with attributes and methods common to all employees.
2. Define Child Classes: We'll create child classes like Manager and Developer that inherit from Employee and add specific behaviors or attributes.

"""

# Step 1: Define the Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working.')

    def get_salary(self):
        return self.salary

# Step 2: Define Child Class for Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        print(f'{self.name} is managing the {self.department} department.')

    def manage(self):
        print(f'{self.name} is managing the team.')

# Step 3: Define Child Class for Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        print(f'{self.name} is writing code in {self.programming_language}.')

    def code(self):
        print(f'{self.name} is coding in {self.programming_language}.')


emp1 = Manager(name='Alice', salary=90000, department='sales')
emp2 = Developer(name='Bob', salary=120000, programming_language='Python')

emp1.work()
print(f'Salary ${emp1.get_salary()} \n')

emp2.work()
print(f'Salary ${emp2.get_salary()} \n')
