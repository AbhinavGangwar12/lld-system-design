"""
Encapsulation in Python

Encapsulation is one of the core concepts of Object Oriented Programming (OOP).

The idea of encapsulation is to bind the data members and methods into a single unit.
Helps in better maintainability, readability and usability as we do not need to explicitly pass data members to member methods
Helps maintain data integrity by allowing validation and control over the values assigned to variables.
It helps in achieving abstraction. A class can hide the implementation part and discloses only the functionalities required by other classes which allows later changes to representations or implementations without impacting the codes that uses this class.
---
Access Specifiers
Access specifiers define how class members (variables and methods) can be accessed from outside the class. 

1. Public Members
Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).

2. Protected members
Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).

3. Private members
Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data. In Python, private members are defined with a double underscore prefix (e.g., self.__salary).
---
Declaring Protected and Private Methods
In Python, you can control method access levels using naming conventions:

Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
Use a double underscore (__) to define a private method accessible only within class due to name mangling.
---

Getter and Setter Methods
In Python, getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:

Read data using a getter method.
Update data using a setter method with optional validation or restrictions.

"""
class Employee:
    def __init__(self, name, salary, department=None):
        self.name = name
        self.__salary = salary # Private attribute
        self._department = department # Protected attribute
    
    # Getter and Setter for salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__validate_salary(new_salary)  # Validate the new salary before setting it
        self.__salary = new_salary
    
    # private method
    def __validate_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
    # protected method, getter for department
    def _get_department(self):
        return self._department
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)
    
    def get_department_info(self):
        return f"Department: {self._get_department()}"  # Accessing protected method from parent class
