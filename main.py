# Importing the Rectangle and Circle classes from shapes.py
from shapes import Rectangle, Circle

# Instantiating objects of Rectangle and Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("Circle Area:", circle.area())
print("Circle Circumference:", circle.perimeter())

def print_details(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Details:")
print_details(rectangle)

print("Circle Details:")
print_details(circle)

q 3.4
def print_details(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Creating instances of Rectangle and Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Calling print_details with instances of Rectangle and Circle
print("Rectangle Details:")
print_details(rectangle)

print("Circle Details:")
print_details(circle)

q3.5 
def print_details(shape):
    print("Details of the shape:")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Creating instances of Rectangle and Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Calling print_details with instances of Rectangle and Circle
print("Rectangle Details:")
print_details(rectangle)

print("\nCircle Details:")
print_details(circle)
