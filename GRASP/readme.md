### GRASP Design Principles in OOAD
In Object-Oriented Analysis and Design (OOAD), General Responsibility Assignment Software Patterns (GRASP) play a crucial role in designing effective and maintainable software systems. GRASP offers a set of guidelines to aid developers in assigning responsibilities to classes and objects in a way that promotes low coupling, high cohesion, and overall robustness.

![GRASP PATTERNS](https://medium.com/@alxkm/grasp-guiding-object-oriented-design-in-java-0f3e4d12a479)

### 1. Creator
Assign the responsibility for creating instances of a class to the class itself or to a related factory class.

>Consider a scenario where you are designing a system for managing a library. In this system, when a new book is added to the library, a `Book` object needs to be created. The responsibility for creating `Book` objects should lie with a class like `Library` or a separate `BookFactory` class. This ensures that the logic for creating `Book` objects is centralized and encapsulated, making it easier to manage.

### 2. Information Expert
Assign a responsibility to the class that has the necessary information to fulfill it.

> Continuing with the library management system, when a user wants to borrow a book, the responsibility of checking if the book is available should lie with the `Book` class itself. The `Book` class contains information about its availability and can perform the necessary checks without needing to rely on other classes. This promotes high cohesion and reduces coupling between classes.

### 3. Low Coupling
Aim for classes to have minimal dependencies on each other.

> In the library management system, suppose there is a `LibraryCatalog` class responsible for managing the catalog of books. Instead of directly accessing the `Book` class to check availability, the `LibraryCatalog` class can rely on an interface, such as `Searchable`, implemented by `Book`. This way, `LibraryCatalog` remains loosely coupled with `Book`, allowing for easier maintenance and changes.

### 4. High Cohension
Ensure that responsibilities within a class are closely related and focused.

> In the library management system, the `Book` class should have cohesive responsibilities related to managing book details, such as title, author, and availability. Responsibilities unrelated to book management, such as user authentication, should be handled by separate classes. This ensures that each class is focused on a specific aspect of the system, promoting clarity and maintainability.

### 5. Controller
Assign the responsibility of handling system events or coordinating activities to a controller class.

> In a web application for a library, when a user requests to borrow a book, the responsibility of handling this request and coordinating the necessary actions should lie with a `BorrowBookController` class. This controller class would interact with other classes, such as `Book`, `User`, and `Library`, to facilitate the borrowing process. By centralizing control logic in a controller class, the system becomes more organized and easier to manage.

### 6. Pure Fabrication
Introduce new classes to fulfill responsiblities without violating cohension and coupling principles.

> Suppose the library management system needs to send email notifications to users when they borrow or return books. Instead of adding email sending logic directly to the `Book` or `User` classes, a separate `NotificationService` class can be created. This `NotificationService` class acts as a pure fabrication responsible for sending email notifications, maintaining low coupling and high cohesion in the system.

### 7. Indirection
Use intermediaries or abstractions to decouple classes and promote flexibilty in design.

> In the library management system, if multiple classes need to access book information, an `BookRepository` interface can be introduced. Classes that need access to book data can depend on the `BookRepository` interface rather than directly on the `Book` class. This allows for flexibility in how book information is retrieved, facilitating easier changes and adaptations in the future.

### 8. Polymorphism
Utilize inheritance and interfaces to enable multiple implementations of behaviors.

> Continuing with the library management system, suppose there are different types of books, such as `FictionBook` and `NonFictionBook`, each with its own borrowing rules. By defining a common interface, `Book`, and implementing it in the `FictionBook` and `NonFictionBook` classes, polymorphism allows the borrowing process to be handled uniformly regardless of the book type. This promotes code reuse and simplifies the handling of different book types within the system.

### IMPORTANCE IN OBJECT-ORIENTED ANALYSIS & DESIGN (OOAD)
+ **Clarity of design** : helps in organizing classes and responsiblities in a way that makes design more understandable.
+ **Low Coupling, High Cohension** : Classes are less dependent on each other which results in more modular and reusable code. Additionally, classes has a clear and focused purpose in the program.
+ **Flexible Design** : Indirection and Polymorphism makes the design more flexible and adaptive to changes.
+ **Scalability** : GRASP patterns makes the desing scalable and adaptive to future changes.
+ **Ease of Maintainance** : With *Pure Fabrication & High Cohension* it becomes very easy to maintain the code as the responsibilities are very clear.
+ **Enhanced Reusability** : creation of classes and objects with well-defined responsibilities and interfaces. This promotes code reusability, as components can be easily reused in different parts of the system or in entirely new projects, leading to increased productivity and reduced development time.