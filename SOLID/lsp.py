from abc import ABC, abstractmethod

class Rectangle(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        return self.width * self.height

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height

    @abstractmethod
    def set_width(self, width):
        self.width = width
    @abstractmethod
    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width
        self.height = width  # Ensure height is the same as width for a square

    def set_height(self, height):
        self.height = height
        self.width = height  # Ensure width is the same as height for a square

if __name__ == "__main__":
    square = Square(5)
    print(f"Initial area of square: {square.area()}")  # Output: 25

# LSP Violation Example
# To see a potential violation of LSP, consider what would happen if you were to use the Square class in a context expecting a Rectangle:
# If you substitute a Square where a Rectangle is expected, changing just the width or height would lead to unexpected results because it will change both dimensions.
