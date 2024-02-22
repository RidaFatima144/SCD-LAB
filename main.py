# Importing the Rectangle and Circle classes from shapes.py
from shapes import Rectangle, Circle

# Instantiating objects of Rectangle and Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("Circle Area:", circle.area())
print("Circle Circumference:", circle.perimeter())
