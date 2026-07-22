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
This principle states that **A class should have only once reason to change** which means every class should have only one single responsibility/job/purpose.

> Example: Imagine a baker who is responsible for baking bread. The baker's role is to focus on the task of baking bread, ensuring that the bread is of high quality, properly baked, and meets the bakery's standards.

+ If the baker handles inventory, ordering, customer service, and cleaning along with baking, it violates SRP since multiple responsibilities are combined.
+ Each task is a separate responsibility, and combining them reduces the baker’s focus and effectiveness in baking.
+ To follow SRP, responsibilities should be divided among different individuals or teams, each handling a specific task independently.

[Check the code example for this princlple](wwww.temp.com)

### 2. Open/Closed Principle
This princple means that **Software Entities (functions, classes, modules etc) should be open for extentions, but closed for modifications** which means you should be able to extent the behavior, without modifying it.

> Example: Imagine you have a class called PaymentProcessor that processes payments for an online store. Initially, the PaymentProcessor class only supports processing payments using credit cards. However, you want to extend its functionality to also support processing payments using PayPal.

+ Instead of modifying the existing PaymentProcessor class, a new PayPalPaymentProcessor class can be created to add PayPal support.
+ This keeps the original class unchanged while extending its functionality through a new class.
+ It follows the Open-Closed Principle by keeping the class closed for modification but open for extension.

[Check the code example for this princlple](wwww.temp.com)

### 3. Liskov's Substitution Principle
Introduced by **Barbar Liskov (1987)** , this princple says that , **derived or child classes should be able to replace their parent classes**. This means that any subclass can be used in-place of their parent/base class without facing any unexpected behaviour by the code.

>Example: One of the classic examples of this principle is a rectangle having four sides. A rectangle's height can be any value and width can be any value. A square is a rectangle with equal width and height. So we can say that we can extend the properties of the rectangle class into square class. 

+ Replacing the Rectangle with a Square forces constraints (equal sides), which changes the expected behavior of the parent class.
+ This violates LSP because a derived class should not alter or break the behavior expected from the base class.

[Check the code example for this princlple](wwww.temp.com)

### 4. Interface Segregation Principle
This principle applies to interfaces and is similar to SRP, focusing on keeping interfaces clean and well-defined. It states that the client should not be forced to depend on the methods that are irrelevant to them, avoiding unnecessary dependencies.

> Example: Suppose if you enter a restaurant and you are pure vegetarian. The waiter in that restaurant gave you the menu card which includes vegetarian items, non-vegetarian items, drinks, and sweets. 

+ Customers should receive a menu relevant to their needs (e.g., vegetarian only) instead of a general menu with unnecessary items.
+ Splitting a common menu into smaller, specific ones reduces unnecessary dependencies and minimizes future changes.

[Check the code example for this princlple](wwww.temp.com)
