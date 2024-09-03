"""
Association

Association is a relationship between two separate classes that are established through their objects. It defines how objects of one class interact with objects of another class.
It can be unidirectional (one object uses or interacts with another) or bidirectional (two objects interact with each other).
Association doesn't imply that one object owns or contains the other; rather, it just implies a connection between the objects.
Unlike aggregation or composition, there is no strict lifecycle management involved. The associated objects can exist independently and do not depend on each other for their existence.

Step-by-step Example:
1. Define Classes for Entities: We'll create Teacher and Student classes.
2. Establish Associations: We'll demonstrate both unidirectional and bidirectional associations between Teacher and Student.

"""

# Step 1: Define Classes for Entities
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}")

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{self.name} is now teaching {student.name}")

# Step 2: Establish Associations

# Unidirectional association example
# Student knows about the courses
student1 = Student("Alice")
student1.add_course("Math")    # Alice is enrolled in Math
student1.add_course("Science") # Alice is enrolled in Science

# Bidirectional association example
# Both Teacher and Student know about each other
teacher1 = Teacher("Mr. Smith")
teacher1.add_student(student1) # Mr. Smith is now teaching Alice

# Example with another student
student2 = Student("Bob")
teacher1.add_student(student2) # Mr. Smith is now teaching Bob

print(f"{teacher1.name} is teaching: {[student.name for student in teacher1.students]}") # Output: Mr. Smith is teaching: ['Alice', 'Bob']
