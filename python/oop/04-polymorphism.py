"""
Polymorphism

Polymorphism literally means "many shapes." In the context of OOP, it allows methods to do different things based on the object it is acting upon, even if they share the same name.
In other words, polymorphism allows us to use a single interface to represent different types of objects. This is typically achieved through method overriding in subclasses or through interfaces/abstract classes.

Step-by-step Example:
1. Define a Parent Class: We'll create a parent class Animal with a method speak().
2. Define Subclasses: We'll create child classes like Dog and Cat that inherit from Animal and override the speak() method.
3. Demonstrate Polymorphism: We'll show how different animal objects can be treated the same way using a common interface.

"""

# Step 1: Define the Parent Class
class Animal:
    def speak(self):
        raise NotImplementedError('Subclass must implement this method')

# Step 2: Define Child Classes with Method Overriding
class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow!'

class Bird(Animal):
    def speak(self):
        return 'Tweet!'

def animal_sound(animal):
    print(animal.speak())

# Step 3: Demonstrate Polymorphism
dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Tweet!
