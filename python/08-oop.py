# Object Oriented Programming
# https://docs.python.org/3/tutorial/classes.html

# Example 1 - Classes
# Classes are a way to group data and functions that operate on that data. They are defined using the class keyword.
# The __init__ method is a special method that is called when an instance of the class is created. It is used to initialize the instance's attributes.
# The self parameter is a reference to the instance itself, and is used to access the instance's attributes and methods.
# The attributes of an instance are accessed using dot notation.
# Methods are functions that are defined inside a class and operate on the instance's data.
# The __str__ method is a special method that is called when the instance is converted to a string, for example when using the print function.

print('#########################')
print('Classes')
print('#########################')

class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model, year, color):
        """ Initialize the Car instance """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.make} {self.model} is driving.")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"


# Create an instance of the Car class
car1 = Car("Toyota", "Corolla", 2020, "Red")
print('car1: Make:', car1.make, 'Model:', car1.model, 'Year:', car1.year, 'Color:', car1.color, 'Wheels:', car1.wheels)
car1.drive()

# Create another instance of the Car class
car2 = Car("Honda", "Civic", 2019, "Blue")
car2.wheels = 5
print('car2: Make:', car2.make, 'Model:', car2.model, 'Year:', car2.year, 'Color:', car2.color, 'Wheels:', car2.wheels)
car2.drive()

# Inheritance
# https://docs.python.org/3/tutorial/classes.html#inheritance
# Inheritance is a way to create a new class that inherits the attributes and methods of an existing class.
# The new class is called a subclass, and the existing class is called a superclass.
# The subclass can override the methods of the superclass, or add new methods.
# The super() function is used to call the superclass's methods.

print('#########################')
print('Inheritance')
print('#########################')

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

    def __str__(self):
        return f"{self.name} ({self.breed})"

    # Overriding the eat method
    def eat(self):
        print(f"{self.name} is eating kibble.")

dog1 = Dog("Buddy", "Golden Retriever")
print('dog1:', dog1)
dog1.eat()

class Frog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def jump(self):
        print(f"{self.name} is jumping.")

    def __str__(self):
        return f"{self.name} ({self.color})"

    # Overriding the eat method
    def eat(self):
        print(f"{self.name} is eating insects.")

frog1 = Frog("Kermit", "Green")
print('frog1:', frog1)

# Multi-level Inheritance
# In multi-level inheritance, a subclass inherits from another subclass.
# The subclass can override the methods of the superclass, or add new methods.
# The super() function is used to call the superclass's methods.

print('#########################')
print('Multi-level Inheritance')
print('#########################')

class Organism:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

class Animal(Organism):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print(f"{self.name} is meowing.")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed})"

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed})"

cat1 = Cat("Whiskers", "Felis catus", "Siamese")
print('cat1:', cat1)

dog1 = Dog("Buddy", "Canis lupus familiaris", "Golden Retriever")
print('dog1:', dog1)

# Multiple Inheritance
# In multiple inheritance, a subclass inherits from multiple superclasses.
# The subclass can override the methods of the superclasses, or add new methods.
# The super() function is used to call the superclasses' methods.

print('#########################')
print('Multiple Inheritance')
print('#########################')

class Prey:
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator:
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} (Prey)"

class Fox(Predator):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} (Predator)"

class Fish(Prey, Predator):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} (Prey, Predator)"

rabbit1 = Rabbit("Bugs")
print('rabbit1:', rabbit1)
rabbit1.flee()

fox1 = Fox("Foxy")
print('fox1:', fox1)
fox1.hunt()

fish1 = Fish("Nemo")
print('fish1:', fish1)
fish1.flee()
fish1.hunt()

# Abstract Classes
# https://docs.python.org/3/library/abc.html
# An abstract class is a class that cannot be instantiated, and is used as a base class for other classes.
# Abstract classes can define abstract methods, which are methods that must be implemented by subclasses.
# The abc module provides the ABC class, which is used to define abstract classes.
# The @abstractmethod decorator is used to define abstract methods.

print('#########################')
print('Abstract Classes')
print('#########################')

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Truck(Vehicle):
    def drive(self):
        print("Truck is driving.")

# vehicle = Vehicle() # TypeError: Can't instantiate abstract class Vehicle with abstract methods drive
car = Car()
car.drive()

truck = Truck()
truck.drive()

# Duck Typing
# https://docs.python.org/3/glossary.html#term-duck-typing
# Duck typing is a style of dynamic typing in which an object's methods and properties determine its type, rather than its class or inheritance hierarchy.
# The name comes from the saying "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
# In Python, duck typing is used to determine an object's type based on its behavior, rather than its class or inheritance hierarchy.

print('#########################')
print('Duck Typing')
print('#########################')

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_sound(animal):
    animal.quack()

duck = Duck()
make_sound(duck)

dog = Dog()
make_sound(dog)

