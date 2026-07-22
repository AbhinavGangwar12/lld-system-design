### SOLID Principles with Real Life Examples
The SOLID principles are five essential guidelines that enhance software design, making code more maintainable and scalable.
- The SOLID principles help in enhancing loose coupling. Loose coupling means a group of classes are less dependent on one another.
- Loose coupling helps in making code more reusable, maintainable, flexible and stable.
- Loosely coupled classes minimize changes in your code when some changes are required in some other code.
### S - SINGLE RESPONSIBILITY
### O - OPEN-CLOSED PRINCIPLE
### L - LISKOV SUBSTITUTION PRINCIPLE
### I - INTERFACE SEGREGATION PRINCIPLE
### D - DEPENDENCY INVERSION PRINCIPLE

## 1. Single Responsibility Principle
This principle states that ***A class should have only once reason to change*** which means every class should have only one single responsibility/job/purpose.
> Example: Imagine a baker who is responsible for baking bread. The baker's role is to focus on the task of baking bread, ensuring that the bread is of high quality, properly baked, and meets the bakery's standards.

+ If the baker handles inventory, ordering, customer service, and cleaning along with baking, it violates SRP since multiple responsibilities are combined.
+ Each task is a separate responsibility, and combining them reduces the baker’s focus and effectiveness in baking.
+ To follow SRP, responsibilities should be divided among different individuals or teams, each handling a specific task independently.

[Check the code example for this princlple]()