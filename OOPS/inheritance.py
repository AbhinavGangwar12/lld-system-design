# Inheritance is a key concept in object-oriented programming that allows one class (child/derived) to inherit the properties and methods of another class (parent/base). This promotes code reusability and improves maintainability.

# Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance in Python:

# 1. Single Inheritance: A child class inherits from a single parent class.
class ParentClass:
    def __init__(self, attribute1):
        self.attribute1 = attribute1

    def parent_method(self):
        return f"Parent Attribute: {self.attribute1}"

class ChildClass(ParentClass): # Single Inheritance
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)  # Call the constructor of the parent class to pass the attribute(s)
        self.attribute2 = attribute2

    def child_method(self):
        return f"Child Attribute: {self.attribute2}"
print("--"*20)
print("Single Inheritance Example:")
print("--"*20)
object1 = ChildClass("value1", "value2")
print(object1.parent_method())  # Accessing method from ParentClass
print(object1.child_method())   # Accessing method from ChildClass
print("--"*20)

# 2. Multiple Inheritance: When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. 

class Base1:
    def __init__(self, attribute1):
        self.attribute1 = attribute1
    def method_base1(self):
        return "Method from Base1"
class Base2:
    def __init__(self, attribute2):
        self.attribute2 = attribute2
    def method_base2(self):
        return "Method from Base2"

class Derived(Base1, Base2): # Multiple Inheritance
    def __init__(self, attribute1, attribute2):
        Base1.__init__(self, attribute1)  # Call the constructor of Base1
        Base2.__init__(self, attribute2)  # Call the constructor of Base2
    def method_derived(self):
        return "Method from Derived"
    
object2 = Derived("value1", "value2")
print("--"*20)
print("Multiple Inheritance Example:")
print("--"*20)
print(object2.method_base1())  # Accessing method from Base1
print(object2.method_base2())  # Accessing method from Base2
print(object2.method_derived())  # Accessing method from Derived
print("--"*20)

# 3. Multilevel Inheritance: When a class is derived from another derived class, it is called multilevel inheritance.
class Level1:
    def __init__(self, attribute1):
        self.attribute1 = attribute1
    def method_level1(self):
        return "Method from Level1"

class Level2(Level1):
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)
        self.attribute2 = attribute2
    def method_level2(self):
        return "Method from Level2"

class Level3(Level2):
    def __init__(self, attribute1, attribute2, attribute3):
        super().__init__(attribute1, attribute2)
        self.attribute3 = attribute3
    def method_level3(self):
        return "Method from Level3"

object3 = Level3("value1", "value2", "value3")
print("--"*20)
print("Multilevel Inheritance Example:")
print("--"*20)
print(object3.method_level1())  # Accessing method from Level1
print(object3.method_level2())  # Accessing method from Level2
print(object3.method_level3())  # Accessing method from Level3
print("--"*20)

# 4. Hierarchical Inheritance: When multiple derived classes inherit from a single base class, it is called hierarchical inheritance.
class Base:
    def __init__(self, attribute1):
        self.attribute1 = attribute1
    def method_base(self):
        return "Method from Base"

class Derived1(Base):
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)
        self.attribute2 = attribute2
    def method_derived1(self):
        return "Method from Derived1"
class Derived2(Base):
    def __init__(self, attribute1, attribute3):
        super().__init__(attribute1)
        self.attribute3 = attribute3
    def method_derived2(self):
        return "Method from Derived2"
class Derived3(Base):
    def __init__(self, attribute1, attribute4):
        super().__init__(attribute1)
        self.attribute4 = attribute4
    def method_derived3(self):
        return "Method from Derived3"

print("--"*20)
print("Hierarchical Inheritance Example:")
print("--"*20)
object4 = Derived1("value1", "value2")
print(object4.method_base())  # Accessing method from Base
print(object4.method_derived1())  # Accessing method from Derived1
object5 = Derived2("value1", "value3")
print(object5.method_base())  # Accessing method from Base
print(object5.method_derived2())  # Accessing method from Derived2
object6 = Derived3("value1", "value4")
print(object6.method_base())  # Accessing method from Base
print(object6.method_derived3())  # Accessing method from Derived3
print("--"*20)

# In Python, the `super()` function is used to call methods from a parent class. It is commonly used in the constructor of a derived class to ensure that the parent class is properly initialized. This is especially important in multiple inheritance scenarios, where you want to ensure that all parent classes are initialized correctly.

# 5. Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance. It allows for more complex relationships between classes, combining the benefits of different inheritance types.

class BaseClass:
    def __init__(self, attribute1):
        self.attribute1 = attribute1
    def method_base(self):
        return "Method from BaseClass"

class IntermediateClass1(BaseClass):
    def __init__(self, attribute1, attribute2):
        BaseClass.__init__(self, attribute1)  # Direct call instead of super()
        self.attribute2 = attribute2
    def method_intermediate1(self):
        return "Method from IntermediateClass1"

class IntermediateClass2(BaseClass):
    def __init__(self, attribute1, attribute3):
        BaseClass.__init__(self, attribute1)  # Direct call instead of super()
        self.attribute3 = attribute3
    def method_intermediate2(self):
        return "Method from IntermediateClass2"

class FinalClass(IntermediateClass1, IntermediateClass2):
    def __init__(self, attribute1, attribute2, attribute3, attribute4):
        IntermediateClass1.__init__(self, attribute1, attribute2)
        IntermediateClass2.__init__(self, attribute1, attribute3)
        self.attribute4 = attribute4
    def method_final(self):
        return "Method from FinalClass"

print("--"*20)
print("Hybrid Inheritance Example:")
print("--"*20)
object7 = FinalClass("value1", "value2", "value3", "value4")
print(object7.method_base())  # Accessing method from BaseClass
print(object7.method_intermediate1())  # Accessing method from IntermediateClass1
print(object7.method_intermediate2())  # Accessing method from IntermediateClass2
print(object7.method_final())  # Accessing method from FinalClass
print("--"*20)

# Method Resolution Order (MRO) is the order in which base classes are searched when executing a method. In Python, MRO follows the C3 linearization algorithm, which ensures a consistent and predictable order of method resolution, especially in multiple inheritance scenarios. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.
print("--"*20)
print("Method Resolution Order (MRO) Example:")
print("--"*20)
print(FinalClass.__mro__)  # Displaying the MRO of FinalClass

# using the super() function to call the constructor of the parent in a multiple inheritance scenario is not recommended because it can lead to unexpected behavior. Instead, it's better to call the constructors of each parent class explicitly, as shown in the Hybrid Inheritance example above. This ensures that each parent class is initialized correctly and avoids potential issues with the MRO.