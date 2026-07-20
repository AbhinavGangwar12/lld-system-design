# Polymorphism means "many forms" and allows the same method, function or operator to behave differently depending on the object or data it works with. This flexibility helps create more reusable, maintainable and scalable code.

'''
Real-Life Example: In a backend payment system, multiple payment options are available such as Credit Card, UPI, NetBanking and Wallet. All payment types use a common method named processPayment() but different implementations:

Credit Card Payment: validates card, talks to bank API
UPI Payment: redirects to UPI gateway
Wallet Payment: checks wallet balance
NetBanking Payment: redirects to bank login

The method name remains the same, but the action changes based on the payment type.
'''

# Types of Polymorphism in Python:

"""
1. Compile-time Polymorphism
Compile-time polymorphism involves selecting a method or operation before program execution, typically through method or operator overloading. Languages such as Java and C++ support this feature.

Python does not support true compile-time polymorphism because method calls are resolved at runtime. However, similar behavior can be achieved using default arguments, variable-length arguments (*args), or keyword arguments (**kwargs).

Example: This code demonstrates overloading-like behavior using default and variable-length arguments. While Python does not support true method overloading, the same method can handle different numbers of arguments.
"""

class Calculator:
    def add(self, a, b=0, *args):
        total = a +b
        if args:
            total += sum(args)
        return total

calci = Calculator()
print("--"*20)
print("Compile-time Polymorphism Example:")
print("--"*20)
print(calci.add(5, 10))  # Output: 15
print(calci.add(5, 10, 15))  # Output: 30
print("--"*20)
print(".")

#example usage of kwargs 
class CalculatorKwargs:
    def add(self, **kwargs):
        total = 0
        for key, value in kwargs.items():
            total += value
        return total

calci_kwargs = CalculatorKwargs()
print("--"*20)
print("Keyword Arguments Polymorphism Example:")
print("--"*20)
print(calci_kwargs.add(a=5, b=10))  # Output: 15
print(calci_kwargs.add(a=5, b=10, c=15))  # Output: 30
print("--"*20)
print(".")

"""
2. Runtime Polymorphism (Overriding)
Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it. This happens through Method Overriding a child class provides its own version of a method already defined in the parent class.
"""

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

print("--"*20)
print("Runtime Polymorphism Example:")
print("--"*20)
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())  # Output will depend on the actual object type
print("--"*20)
print(".")
# Polymorphism with Operators and built-in functions
# Python supports operator overloading, allowing the same operator to have different meanings based on the context
print("--"*20)
print("Operator Overloading Example:")
print("--"*20)

print(5 + 10)  # Output: 15 (integer addition)
print("Hello " + "World")  # Output: Hello World (string concatenation)
print("--"*20)
print(".")
print("--"*20)
print("Built-in Function Overloading Example:")
print("--"*20)
print(len("Hello"))  # Output: 5 (length of string)
print(len([1, 2, 3, 4]))  # Output: 4 (length of list)
print("--"*20)
print(".")

# Method Overriding in Python
# Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This is a key feature of runtime polymorphism.
class Parent:
    def show_message(self):
        return "Message from Parent class"
class Child(Parent):
    def show_message(self):
        return "Message from Child class"
print("--"*20)
print("Method Overriding Example:")
print("--"*20)
parent_obj = Parent()
child_obj = Child()
print(parent_obj.show_message())  # Output: Message from Parent class
print(child_obj.show_message())  # Output: Message from Child class
print("--"*20)
print(".")


# Method overriding with constructors
class ParentConstructor:
    def __init__(self):
        self.message = "Message from Parent Constructor"
    def show_message(self):
        return self.message
class ChildConstructor(ParentConstructor):
    def __init__(self):
        super().__init__()  # Call the parent constructor
        self.message = "Message from Child Constructor"
    def show_message(self):
        return self.message

print("--"*20)
print("Constructor Overriding Example:")
print("--"*20)
parent_constructor_obj = ParentConstructor()
child_constructor_obj = ChildConstructor()
print(parent_constructor_obj.show_message())  # Output: Message from Parent Constructor
print(child_constructor_obj.show_message())  # Output: Message from Child Constructor
print("--"*20)
print(".")

# Similary, method overriding works with multiple inheritance as well. The method resolution order (MRO) determines which method is called when there are multiple parent classes. Python uses the C3 linearization algorithm to determine the MRO. The same case applies to method overriding in multi-level inheritance. The method in the most derived class is called, and if it doesn't exist, Python looks up the hierarchy until it finds the method or reaches the base class.

"""
Method Calls Inside Parent Class
A parent class method can call another method using self. If that second method is overridden in the child class, Python automatically executes the child class version. This behavior is a key part of runtime polymorphism.
"""

class ParentWithMethod:
    def generate(self):
        print("Generating from Parent class")
        self.display()
    def display(self):
        print("Displaying from Parent class")
class ChildWithMethod(ParentWithMethod):
    def display(self):
        print("Displaying from Child class")

print("--"*20)
print("Method Calls Inside Parent Class Example:")
print("--"*20)
obj = ChildWithMethod()
obj.generate()  # Output will show that the display method from Child class is called
print("--"*20)
print(".")

# We can call the parent class method using super() / className to avoid the overridden method in the child class. This is useful when we want to ensure that the parent class's implementation is executed, even if a child class has overridden that method.


# Operator Overloading with User defined classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #addition operator overloading
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    #comparison operator overloading
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print("--"*20)
print("Operator Overloading with User Defined Classes Example:")
print("--"*20)
print(p1 + p2)  # Output: Point(4, 6)
print(p1 == p2)  # Output: False
print("--"*20)
print(".")


"""
Binary Operators
Operator	Magic Method
+	--> __add__(self, other)
-	--> __sub__(self, other)
*	--> __mul__(self, other)
/	--> __truediv__(self, other)
//	--> __floordiv__(self, other)
%	--> __mod__(self, other)
**	--> __pow__(self, other)


Comparison Operators
Operator	Magic Method
<	--> __lt__(self, other)
>	--> __gt__(self, other)
<=	--> __le__(self, other)
>=	--> __ge__(self, other)
==	--> __eq__(self, other)
!=	--> __ne__(self, other)

Assignment Operators
Operator	Magic Method
-=	--> __isub__(self, other)
+=	--> __iadd__(self, other)
*=	--> __imul__(self, other)
/=	--> __itruediv__(self, other)
//=	--> __ifloordiv__(self, other)
%=	--> __imod__(self, other)
**=	--> __ipow__(self, other)


Unary Operators
Operator	Magic Method
-	--> __neg__(self)
+	--> __pos__(self)
~	--> __invert__(self)
"""