# classes are blueprints for creating objects. They define the attributes and methods that the objects created from the class will have.
class ClassName:
    def __init__(self, attribute1, attribute2): # this is the constructor method
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self): # these are instance methods
        return f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}"

    def method2(self, new_value):
        self.attribute1 = new_value
        return f"Attribute 1 updated to: {self.attribute1}"
    
# self is a reference to the current instance of the class and is used to access variables that belong to the class.

# Objects are instances of classes. Each object can have its own attributes and methods, which can be accessed and modified independently of other objects.

object1 = ClassName("value1", "value2") # creating an object of the class
print(object1.method1()) # calling method1 on object1