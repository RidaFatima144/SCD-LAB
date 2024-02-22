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

q3.6
from data_structures import DataProcessor


    data_processor = DataProcessor()

    # Testing sort_data method
    tuple_data = (5, 2, 8, 1, 3)
    print("Sorted Tuple:", data_processor.sort_tuple(tuple_data))

    list_data = [10, 20, 30]
    print("Sorted List:", data_processor.append_list(list_data, 40))

    dict_data = {'b': 2, 'a': 1, 'c': 3}
    print("Sorted Dictionary:", data_processor.update_dictionary(dict_data, 'd', 4))

    set_data = {5, 2, 8, 1, 3}
    print("Sorted Set:", data_processor.remove_from_set(set_data, 3))

    # Testing append_data method
    list_data = [10, 20, 30]
    print("Appended List:", data_processor.append_list(list_data, 40))

    set_data = {1, 2, 3}
    print("Appended Set:", data_processor.append_list(set_data, 4))

    # Testing update_data method
    dict_data = {'a': 1, 'b': 2, 'c': 3}
    print("Updated Dictionary:", data_processor.update_dictionary(dict_data, 'd', 4))

    # Testing remove_data method
    list_data = [10, 20, 30]
    print("List with Element Removed:", data_processor.remove_from_set(list_data, 20))

    set_data = {1, 2, 3, 4, 5}
    print("Set with Element Removed:", data_processor.remove_from_set(set_data, 3))
