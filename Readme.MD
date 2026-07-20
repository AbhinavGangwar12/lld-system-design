# Chapter 1: Basic Class and Object


## 1. Introduction


Welcome to the world of Object-Oriented Programming (OOP). Before we dive into the syntax and code, we must first understand how to think in OOP.

What is this concept?

In traditional programming (called Procedural Programming), you write code as a sequence of steps. You create variables to hold data, and you write functions to modify that data. The data and the functions are separate.

Object-Oriented Programming (OOP) is a paradigm—a way of thinking about and organizing code. Instead of separating data and functions, OOP combines them into a single, logical unit called an Object.

A Class is the blueprint for creating these objects.

An Object is a specific instance created from that blueprint.

Why was it introduced?

As software grew larger and more complex in the 1970s and 1980s, procedural programming became difficult to manage. Variables were scattered everywhere, and thousands of functions were modifying global data. If you changed a variable's structure in one place, fifty different functions would break.

OOP was introduced to solve this chaos by bundling data and the functions that operate on that data together. This makes code modular, reusable, and much easier to debug.

What problem does it solve?

Spaghetti Code: It prevents data from being modified unexpectedly by unrelated parts of a program.

Reusability: You can write a class once and generate millions of objects from it.

Real-World Modeling: It allows programmers to map real-world entities (like a User, a BankAccount, or an Enemy) directly into code.

Where is it used in real software?

Literally everywhere. When you click a button on a website, that button is an object. In a video game, the player, the enemies, the weapons, and the trees are all objects. In a banking application, every customer's account is a separate object generated from a BankAccount class.

## 2. Real World Analogy


To understand Classes and Objects, let's look at two real-world analogies.

### Analogy 1: The Architect and the House


Imagine you want to build a house. You don't just start stacking bricks. First, you hire an architect.

The Class is the architectural blueprint. It exists on paper. It defines that the house will have 3 bedrooms, 2 windows, and 1 door. You cannot live inside a blueprint.

The Object is the actual physical house built using that blueprint. You can build 100 identical houses from that single blueprint. Each house is a separate object. If you paint House A blue, House B does not suddenly turn blue. They share the same design, but they are independent entities.

### Analogy 2: The Cookie Cutter and the Cookies


The Class is the cookie cutter. It defines the shape (e.g., a star).

The Objects are the cookies themselves. Once you cut the dough and bake the cookies, you have multiple objects. Some might have chocolate chips added to them, some might have sprinkles, but they all originated from the same cookie cutter.

Important

A Class is just a design. It takes up almost no memory. An Object is the actual realization of that design, which holds real data and takes up memory.

## 3. Core Theory


Let's explore the core theory behind classes and objects.

### Definition


Class: A user-defined data type that acts as a blueprint for objects. It defines the structure (attributes) and behavior (methods) that its objects will have.

Object: An instance of a class. It has state (data) and behavior (actions).

Instantiation: The process of creating an object from a class.

### Purpose


The primary purpose of a class is to encapsulate (bundle) related data and behaviors into a single package, making the codebase structured and mirroring real-world logic.

### Advantages


Modularity: Code is divided into self-contained objects.

Data Hiding: Objects can protect their internal data from outside interference.

Maintainability: Fixing a bug in a class fixes it for all objects of that class.

### Disadvantages


Steep Learning Curve: Thinking in objects is initially harder for beginners.

Boilerplate Code: OOP can sometimes require more lines of code for simple tasks compared to procedural programming.

Memory Overhead: Objects take up slightly more memory than simple primitive variables.

Internal Working & Memory Behavior

When you define a class in Python, Python creates a class object in memory. However, no actual instance data is created yet.
When you create an object (instantiation), Python requests memory from the operating system (specifically, the Heap) to store the data for that specific object. Each object gets its own unique memory address.

Common Misconceptions

Misconception: A class holds data.

Fact: A class holds the structure. The object holds the data.

## 4. Syntax Breakdown


Let's look at the absolute most basic syntax for creating a class and an object in Python.

class Student:
    pass

student1 = Student()


### Breakdown of the Class Definition:


class: This is a Python keyword. It tells Python, "I am about to define a new blueprint."

Student: This is the name of the class. By convention, class names should be written in PascalCase (capitalizing the first letter of every word, with no underscores).

: (colon): Indicates the start of the class's body.

Indentation: Everything indented under the class belongs to that class.

pass: A keyword that means "do nothing." We use it here because Python expects something inside the class, but we aren't ready to add data yet.

### Breakdown of Object Creation (Instantiation):


student1: This is just a variable name. It will hold the reference to our new object.

=: The assignment operator.

Student: We are calling the class name.

(): The parentheses are crucial! They tell Python to execute the creation process and build a new object in memory.

## 5. Visual Diagrams (ASCII)


Blueprint to Object Generation

+-----------------------+
| CLASS: Student        |  <--- The Blueprint (Memory: Code Space)
+-----------------------+
| - Needs a name        |
| - Needs an age        |
+-----------------------+
          |
          | (Instantiation with ())
          v
+-----------------------+       +-----------------------+
| OBJECT 1              |       | OBJECT 2              |
+-----------------------+       +-----------------------+
| Memory Addr: 0x10A    |       | Memory Addr: 0x10B    |
| name = "Alice"        |       | name = "Bob"          |
| age = 20              |       | age = 22              |
+-----------------------+       +-----------------------+
      ^                               ^
      |                               |
  student1                        student2  <--- Variable references


How Variables point to Objects

Variable `student1` --------> [ Object Data inside Heap Memory ]
(Stack Memory)                (Heap Memory)


## 6. Step-by-Step Code Examples


Let's start from absolute zero and slowly build up.

### Example 1: The Empty Class


### Explanation: The simplest class possible.


#### Code

```python
class Car:
    pass
```

# Creating an object
my_car = Car()

print(my_car)


### Expected Output:

<__main__.Car object at 0x7f8b9c0b5a90> (Your memory address will differ)

Why it works: Python successfully created a Car object in memory. Printing it shows the class name and its physical location in your computer's RAM.

Time Complexity: $O(1)$

Space Complexity: $O(1)$

### Example 2: Adding Attributes (Data) Manually


### Explanation: Objects are useless without data. Data attached to an object is called an attribute. Here, we add attributes after creating the object.


#### Code

```python
class Car:
    pass
```

car1 = Car()
car1.color = "Red"      # Creating an attribute called 'color'
car1.brand = "Toyota"   # Creating an attribute called 'brand'

print(car1.color)
print(car1.brand)


### Expected Output:


Red
Toyota


Execution Flow: We create car1. Then, using dot notation (.), we reach inside car1 and create a variable color and assign it "Red".

### Example 3: Multiple Independent Objects


### Explanation: Proof that objects do not share data.


#### Code

```python
class Car:
    pass
```

car1 = Car()
car1.brand = "Ford"

car2 = Car()
car2.brand = "Honda"

print("Car 1 is a:", car1.brand)
print("Car 2 is a:", car2.brand)


### Expected Output:


Car 1 is a: Ford
Car 2 is a: Honda


Why it works: car1 and car2 live at completely different memory addresses. Modifying car2 has zero effect on car1.

### Example 4: The Constructor (__init__)


### Explanation: Adding attributes manually (like in Ex 2) is bad practice. We might forget to add them. Instead, we use a special setup method called __init__ (short for initialization), known as the constructor. It runs automatically the moment the object is created.

(Note: We will cover self deeply in Chapter 2, but for now, know that self simply means "the specific object being created right now").

#### Code

```python
class Book:
    def __init__(self):
        # This code runs automatically when a Book() is created
        self.title = "Unknown Title"
        self.pages = 100
```

book1 = Book()
print(book1.title)
print(book1.pages)


### Expected Output:


Unknown Title
100


Execution Flow: We call Book(). Python creates a blank object in memory. Python immediately feeds this blank object into the __init__ method as self. We then attach .title and .pages to it.

### Example 5: Passing Dynamic Values to the Constructor


### Explanation: Hardcoding "Unknown Title" isn't very useful. Let's pass our own data when we create the object.


#### Code

```python
class Book:
    def __init__(self, book_title, book_pages):
        self.title = book_title
        self.pages = book_pages
```

# We must pass the arguments inside the parentheses now!
book1 = Book("Harry Potter", 400)
book2 = Book("Python Crash Course", 600)

print(book1.title, "-", book1.pages)
print(book2.title, "-", book2.pages)


### Expected Output:


Harry Potter - 400
Python Crash Course - 600


### Example 6: Default Parameter Values


### Explanation: What if we want to pass data, but also have a fallback if we don't? We use default arguments.


#### Code

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
```

acc1 = BankAccount("Alice", 500) # Provided balance
acc2 = BankAccount("Bob")        # Relies on default balance

print(acc1.owner, "has $", acc1.balance)
print(acc2.owner, "has $", acc2.balance)


### Expected Output:


Alice has $ 500
Bob has $ 0


### Example 7: Modifying Attributes


### Explanation: You can change an object's attributes at any time using dot notation.


#### Code

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

emp = Employee("John", 50000)
print("Before promotion:", emp.salary)

# Modifying the attribute
emp.salary = 60000
print("After promotion:", emp.salary)


### Expected Output:


Before promotion: 50000
After promotion: 60000


### Example 8: Deleting Attributes


### Explanation: You can completely remove an attribute from an object using the del keyword.


#### Code

```python
class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0
```

player1 = Player("Gamer99")
print(player1.username)

# Delete the score attribute
del player1.score

# Trying to print it will crash the program (AttributeError)
# print(player1.score)


### Example 9: Objects interacting with other objects


### Explanation: Objects can interact. An attribute of one object can be a completely different object!


#### Code

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
```

class Car:
    def __init__(self, brand, engine_object):
        self.brand = brand
        self.engine = engine_object  # Storing an object inside another object

v8_engine = Engine(500)
my_car = Car("Ford Mustang", v8_engine)

# Accessing the engine's horsepower through the car
print(f"{my_car.brand} has {my_car.engine.horsepower} HP")


### Expected Output:


Ford Mustang has 500 HP


### Example 10: Lists of Objects


### Explanation: Just like you can have a list of integers, you can have a list of objects.


#### Code

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog3 = Dog("Max")

# Store them in a list
pack = [dog1, dog2, dog3]

# Loop through the list
for dog in pack:
    print("Good boy,", dog.name)


### Expected Output:


Good boy, Rex
Good boy, Buddy
Good boy, Max


## 7. Under the Hood


What is Python doing internally when you deal with objects?

Everything is an Object: In Python, even integers, strings, and lists are objects. When you write x = 5, 5 is actually an object of the <class 'int'>. You can verify this by typing print(type(5)).

The __dict__ magic: How does an object remember its attributes? Under the hood, Python objects store all their attributes in a standard dictionary (hash map). You can view this dictionary using the __dict__ attribute.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_cat = Cat("Whiskers", 3)
print(my_cat.__dict__)
# Output: {'name': 'Whiskers', 'age': 3}


Memory Allocation: When you call Cat("Whiskers", 3), Python's memory manager finds free space on the Heap, stores the dictionary {'name': 'Whiskers', 'age': 3}, and returns the memory address (reference) to the variable my_cat.

## 8. Common Beginner Mistakes


Here are the top 10 mistakes beginners make with basic classes and objects.

### Mistake 1: Forgetting parentheses during instantiation


- ❌ Wrong: car = Car (Assigns the blueprint itself to the variable)
- ✅ Right: car = Car() (Creates an object)

### Mistake 2: Forgetting self in __init__


- ❌ Wrong: def __init__(name): (Python will crash saying it takes 1 argument but 2 were given)
- ✅ Right: def __init__(self, name):

### Mistake 3: Improper Indentation


- ❌ Wrong:

class Dog:
def __init__(self):
    pass


- ✅ Right: Methods must be indented inside the class.

### Mistake 4: Using lowercase for Class names


- ❌ Wrong: class student: (This runs, but violates professional coding standards).
- ✅ Right: class Student: (PascalCase).

### Mistake 5: Misspelling __init__


- ❌ Wrong: def _init_(self): or def __int__(self): (Python will not recognize this as the constructor and will not run it automatically).
- ✅ Right: def __init__(self): (Two underscores on both sides).

### Mistake 6: Trying to access attributes before they exist


- ❌ Wrong:

class User: pass
u = User()
print(u.name) # Crashes: AttributeError


- ✅ Right: Always initialize attributes in __init__.

### Mistake 7: Creating new attributes by typo


- ❌ Wrong:

car1 = Car()
car1.color = "Red"
car1.colr = "Blue" # Typo creates a brand new, useless attribute!


- ✅ Right: Python will not warn you if you misspell an attribute name during assignment. Be careful!

### Mistake 8: Thinking Objects share attributes


- ❌ Wrong: Believing that changing car1.color will change car2.color.
- ✅ Right: Every instance maintains its own independent state.

### Mistake 9: Printing an object and expecting its data


- ❌ Wrong: print(student1) outputs <__main__.Student object at 0x...>
- ✅ Right: You must print specific attributes: print(student1.name). (Later chapters will teach you __str__ to fix this).

### Mistake 10: Treating classes like dictionaries


- ❌ Wrong: student1["name"] = "Alice"
- ✅ Right: student1.name = "Alice" (Use dot notation).

## 9. Best Practices


To write professional, production-ready Python code, follow these rules:

Naming Conventions (PEP 8):

Classes: PascalCase (e.g., BankAccount, PlayerCharacter).

Objects/Instances: snake_case (e.g., my_account, player_one).

Attributes: snake_case (e.g., first_name, max_health).

Always use __init__: Never add attributes dynamically from outside the class (like obj.name = "X"). Always define the entire structure of the object inside the __init__ method. This makes your code predictable.

Single Responsibility Principle: A class should only represent one concept. Don't create a CustomerAndBankAndDatabase class. Create three separate classes.

Keep __init__ simple: The constructor should only initialize variables. It should not contain heavy logic like downloading files from the internet or running infinite loops.

## 10. Real Projects


Where do basic classes and objects appear in real software?

Django / Web Development: In Django (a Python web framework), every table in a database is represented as a Class, and every row in that database table is an Object.

Game Development (Pygame): Every enemy on the screen is an object created from an Enemy class. It has attributes like .x, .y, and .health.

APIs: When you fetch weather data from an API, a professional codebase will convert that messy JSON text into a clean Weather object with attributes like .temperature and .humidity.

## 11. Interview Questions


### Theory Questions


What is OOP? Object-Oriented Programming, a paradigm that organizes software design around data, or objects, rather than functions and logic.

What is a Class? A blueprint or template for creating objects.

What is an Object? An instance of a class that exists in memory and holds actual data.

What is Instantiation? The process of creating an object from a class.

What is the difference between a Class and an Object? A class is logical (takes no memory for data), an object is physical (takes heap memory).

What is an Attribute? A variable bound to a specific object (its state).

What is a Method? A function defined inside a class (its behavior). (Covered deeply in Chap 2)

What is __init__? The constructor method that runs automatically upon object creation.

Why are there double underscores in __init__? Python uses double underscores (dunder) for special, built-in magic methods.

Does a class take up memory? Yes, a small amount in the code segment, but it does not take up instance data memory.

Are everything objects in Python? Yes, numbers, strings, and even functions are objects.

What does type() do? Returns the class that an object was instantiated from.

What does the pass keyword do? Acts as a placeholder to prevent IndentationErrors in empty classes.

How do you access an object's attributes? Using dot notation (object.attribute).

Can objects of the same class have different attributes? Yes, technically you can dynamically add attributes to just one object, though it is bad practice.

### Coding Questions


Write an empty class Car and create an object my_car.

class Car: pass
my_car = Car()


Write a class Person with name and age initialized in __init__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Create an object of Person and print its age.

p = Person("Alice", 30)
print(p.age)


Change the age of the previous object to 31.

p.age = 31


Delete the name attribute of the object.

del p.name


Write a class Rectangle with a default width of 10 and height of 5.

class Rectangle:
    def __init__(self, width=10, height=5):
        self.width = width
        self.height = height


Create a list containing 3 distinct Rectangle objects.

rects = [Rectangle(), Rectangle(2,2), Rectangle(3,4)]


Write a loop to print the width of all rectangles in the list.

for r in rects: print(r.width)


Create a Smartphone class with brand. Create two phones. Prove they are at different memory addresses.

class Smartphone:
    def __init__(self, brand):
        self.brand = brand
p1 = Smartphone("Apple")
p2 = Smartphone("Samsung")
print(id(p1) == id(p2)) # Prints False


Print the internal dictionary of p1.

print(p1.__dict__)


Tricky Conceptual Questions

Q: What happens if you return a value from __init__?
A: It throws a TypeError. The __init__ method must always return None. Its only job is to initialize the object.

Q: If a = Book() and b = a, how many objects were created?
A: Only ONE object was created. b = a just creates a second variable pointing to the exact same memory address. Changing b.title will change a.title.

Q: Can you name the first parameter in __init__ something other than self?
A: Yes, you can name it this, me, or x. But doing so violates Python conventions. Always use self.

Q: Is __init__ technically the method that creates the object?
A: No. __new__ creates the object in memory. __init__ is called after creation to initialize variables.

Q: If I delete an object using del obj, is the memory instantly freed?
A: Python uses a Garbage Collector. The memory is freed when the reference count drops to zero.

## 12. Practice Problems


### Easy


Create a class Planet. Create an object earth from it.

Add an attribute name to earth manually without using __init__.

Create a class Computer with an __init__ method that accepts cpu and ram. Create an object.

Print the ram of your Computer object.

Change the ram of your object to a higher number.

### Medium


Create a Movie class with title, director, and rating. Create 3 movie objects and store them in a list.

Loop through the list of movies. If a movie's rating is greater than 8.0, print its title.

Create a class Wallet with balance defaulting to 0. Create an object. Add 50 to the balance using standard arithmetic (+=).

Prove that two objects created with the exact same data (w1 = Wallet(50), w2 = Wallet(50)) are not the same object in memory.

Print the __dict__ of a movie object.

### Hard


Create a School class that accepts a name. Create a Student class that accepts a name and a school_object. Create a school, then create a student and assign the school object to the student. Print the student's school's name.

Write a script that instantiates 100 Enemy objects in a list using a for loop. Give each enemy a unique ID from 1 to 100.

Create a class DatabaseConnection. Demonstrate how multiple variables can point to the same instantiated object, and modifying an attribute through one variable affects the other.

Write a class that intentionally crashes by returning a string inside __init__. Observe the error.

Try to access an attribute that hasn't been created yet. Catch the error using a try-except block.

### Very Hard


Create a dictionary where the keys are strings ("Warrior", "Mage") and the values are actual Classes (not objects). Write code that asks the user for input, looks up the Class in the dictionary, and instantiates an object of that class.

Investigate the id() function. Create an object, check its id(), delete the object using del, create a new object immediately, and check its id(). Are they the same? Why?

Build a simple class Point with x and y. Write a standalone function outside the class that takes two Point objects and calculates the distance between them using the Pythagorean theorem.

Research Python's setattr() and getattr() built-in functions. Use them to add and read an attribute from an object dynamically.

What happens if you define two __init__ methods inside the same class? Write the code and explain the output.

(Solutions not provided per constraints. Challenge yourself!)

## 13. Mini Project: Basic Character Generator


Let's combine everything we've learned into a small executable script. We will build a character generator for a basic Role Playing Game (RPG).

#### Code

```python
```

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Character:
    def __init__(self, name, char_class, starting_weapon):
        self.name = name
        self.char_class = char_class
        self.health = 100
        self.level = 1
        self.weapon = starting_weapon # Storing a Weapon object inside Character

# 1. Create our weapons
sword = Weapon("Iron Sword", 15)
staff = Weapon("Wooden Staff", 8)

# 2. Create our characters, passing the weapons to them
player1 = Character("Arthur", "Knight", sword)
player2 = Character("Merlin", "Wizard", staff)

# 3. Output their data
print("--- RPG CHARACTER PROFILES ---")

print(f"Name: {player1.name}")
print(f"Class: {player1.char_class}")
print(f"Health: {player1.health} HP")
print(f"Weapon: {player1.weapon.name} (Damage: {player1.weapon.damage})")

print("------------------------------")

print(f"Name: {player2.name}")
print(f"Class: {player2.char_class}")
print(f"Health: {player2.health} HP")
print(f"Weapon: {player2.weapon.name} (Damage: {player2.weapon.damage})")


### Expected Output:


--- RPG CHARACTER PROFILES ---
Name: Arthur
Class: Knight
Health: 100 HP
Weapon: Iron Sword (Damage: 15)
------------------------------
Name: Merlin
Class: Wizard
Health: 100 HP
Weapon: Wooden Staff (Damage: 8)


### Explanation:


We define two blueprints: Weapon and Character.

Weapon just holds name and damage.

Character holds name, class, health (defaulting to 100), level (defaulting to 1), and a weapon.

We instantiate the weapons first so they exist in memory.

We instantiate the characters, passing the weapon objects into the character's constructor. This is called composition (a character "has a" weapon).

## 14. Summary


### Concept


### Explanation


OOP

Object-Oriented Programming, organizing code by grouping data and behavior.

Class

The blueprint/template used to create objects.

Object

A physical instance created from a class, occupying heap memory.

Instantiation

The act of creating an object: obj = ClassName().

Attribute

A variable that belongs to a specific object (its data/state).

__init__

The constructor method that automatically runs when an object is created.

Dot Notation

The syntax used to access or modify attributes: object.attribute.

## 15. Cheat Sheet


Define a Class:

class Dog:
    pass


Define a Constructor:

class Dog:
    def __init__(self, name):
        self.name = name


Instantiate an Object:

my_dog = Dog("Rex")


Access Data:

print(my_dog.name)


Modify Data:

my_dog.name = "Max"


### Important Rules:


class names use PascalCase.

Always include self as the first parameter in __init__.

Parentheses () trigger instantiation.

## 16. Advanced Notes


Connecting to Chapter 2: In this chapter, we focused solely on State (Attributes/Data). However, real-world objects don't just sit there; they do things. A Car drives, a Dog barks, a Bank Account deposits money. In the next chapter (Class Methods and Self), we will learn how to attach functions inside classes so our objects can perform actions. We will also deep-dive into exactly what the magical self keyword is and how it powers all of OOP.

Metaclasses (Advanced): We learned that objects are created from Classes. But what creates a Class? In Python, classes themselves are objects created by a higher-level class called a Metaclass (specifically, type). You don't need to worry about this until you reach very advanced Python architecture!