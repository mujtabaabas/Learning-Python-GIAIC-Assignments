from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# ---- demo ----
if __name__ == "__main__":
    # shape = Shape()  # This will raise an error: Can't instantiate abstract class

    rect = Rectangle(5, 10)
    print("Rectangle area:", rect.area())
