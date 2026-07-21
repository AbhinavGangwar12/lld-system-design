"""
Abstraction in Python

Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user. It is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

Real Life Example: In a graphics software, multiple shapes are available such as Circle, Rectangle and Triangle. All shapes share common data and support the same set of actions, but the internal details are hidden:

Common data: name, color, border thickness, fill style.
Common actions: draw(), resize(), getArea().
Each shape implements these actions differently Circle uses radius, Rectangle uses length and width and Triangle uses base and height.
The software only knows that a shape can be drawn and its area can be calculated. How the shape is drawn or how the area is calculated is hidden
"""

# Abstract Base Class (ABC) - used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.

# Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a Circle with radius {self.radius}"

    def get_area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.draw())  # Output: Drawing a Circle with radius 5
print(c.get_area())  # Output: 78.5


"""
Components of Abstraction
Abstraction is made up of key components, these elements work together to define a clear and enforced structure for subclasses while hiding unnecessary implementation details

1. Abstract Method
Abstract methods are method declarations without a body defined inside an abstract class. They act as placeholders that force subclasses to provide their own specific implementation, ensuring consistent structure across derived classes.
"""

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass 

"""
2. Concrete Method
Concrete methods are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality.
"""

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        return "Sleeping..."

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound())  # Output: Bark
print(dog.sleep())  # Output: Sleeping...

"""
3. Abstract Properties
Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties.
"""

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # Output: 78.5

"""
4. Abstract Class Instantiation
Abstract classes cannot be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations. Attempting to instantiate an abstract class results in a TypeError.
"""