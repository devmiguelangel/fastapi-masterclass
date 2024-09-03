"""
Composition

Composition is a design principle where a class is composed of one or more objects of other classes, rather than inheriting from them. In other words, instead of using "is-a" relationships (inheritance), composition uses "has-a" relationships.
It involves creating objects that have references to other objects, thus allowing you to build complex behaviors by combining different classes.
This method promotes code reuse and can make your code more maintainable and flexible, as it allows for greater control over how objects interact.

Step-by-step Example:
1. Define Simple Classes for Components: We'll create separate classes for components like Engine, Tire, and SteeringWheel.
2. Define a Complex Class: We'll define a Car class that uses composition to include instances of these component classes as attributes.

"""

# Step 1: Define Simple Classes for Components
class Engine:
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')

class Tire:
    def inflate(self):
        print('Tire inflated')

    def deflate(self):
        print('Tire deflated')

class SteeringWheel:
    def left(self):
        print('Turned left')

    def right(self):
        print('Turned right')

# Step 2: Define a Complex Class Using Composition
class Car:
    def __init__(self):
        self.engine = Engine()
        self.tires = [Tire() for _ in range(4)]
        self.steering_wheel = SteeringWheel()

    def start(self):
        self.engine.start()

        for tire in self.tires:
            tire.inflate()

        print('Car is ready to go!')

    def stop(self):
        self.engine.stop()

        for tire in self.tires:
            tire.deflate()

        print('Car stopped')

    def turn_left(self):
        self.steering_wheel.left()

    def turn_right(self):
        self.steering_wheel.right()


# Create an instance of the Car class
car = Car()
car.start()
car.turn_left()
car.turn_right()
car.stop()
