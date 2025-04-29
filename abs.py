'''
this part of code explains how abstaction work in python hides the 
internal details and shows only the essential features of the object.
An abstract class is a class that cannot be instantiated. It is meant to be subclassed by other classes that implement the abstract methods and properties.
abstract class is a blueprint for other classes. It is a template for creating subclasses. An abstract class is a class that cannot be instantiated. 
It is meant to be subclassed by other classes that implement the abstract methods and properties.
And about abstract methods, an abstract method is a method that is declared but contains no implementation.
Defined using @abstractmethod decorator comes from abc module cannot be called on its own.
'''
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def __init__(self, radius):
        pass  # Abstract constructor, no implementation here

    @abstractmethod
    def area(self):
        pass  # Abstract method

    def description(self):  # Concrete method
        return "This is a shape"

class Circle(Shape):  # Subclass of Shape
    def __init__(self, radius):  # Concrete constructor
        self.radius = radius  # Initializing instance attribute
        print("Circle constructor")

    def area(self):
        return 3.14 * self.radius ** 2  # Implementing abstract method

# Create a Circle object
circle = Circle(5)
print(circle.area())  # Output: 78.5
print(circle.description())  # Output: This is a shape
