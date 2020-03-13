# Abstract class code.
# Importing reqiured modules.
from abc import ABC
import math

 # Abstract class
class Shape(ABC):
    
     # Empty functions.
     def calculateArea(self):
          pass

     def calculatePerimeter(self):
          pass

     def noofsides(self):
          pass

# Will display details about square.
class Square(Shape):
     _side = int(input("Enter the length of side: "))  # Data for Square.

     # Will calculate Area.
     def calculateArea(self):
          print(f"The area of the square is {Square._side ** 2}.")

      # Will calculate perimeter.
     def calculatePerimeter(self):
          print(f"The perimeter of the square if {4 * Square._side}.")

     # Will tell number of sides
     def noofsides(self):
          print(f"The number of sides is 4.")

# The rest classes and methods are created in the same type.
class Rectangle(Shape):

     _length = int(input("Enter the length: "))
     _breadth = int(input("Enter the breadth: "))

     def calculateArea(self):
          print(f"The area of the square is {Rectangle._length * Rectangle._breadth}.")

     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2 * (Rectangle._length + Rectangle._breadth)}.")

     def noofsides(self):
          print(f"The number of sides is 4.")

class Circle(Shape):

     _radius = int(input("Enter the radius: "))

     def calculateArea(self):
          print(f"The area of the square is {math.pi * Circle._radius ** 2}.")

     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2 * math.pi * Circle._radius}.")

     def noofsides(self):
          print(f"It's a circle so there are infinite sides.")

class Ellipse(Shape):

     _x_axis_length = int(input("Enter x-axis length: "))
     _y_axis_length = int(input("Enter y-axis length: "))

     def calculateArea(self):
          print(f"Area of ellipse is {math.pi * Ellipse._x_axis_length * Ellipse._y_axis_length}")
          
     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2  * math.pi * math.sqrt(((Ellipse._x_axis_length**2) + (Ellipse._y_axis_length ** 2))/2)}.")

     def noofsides(self):
          print(f"It's an ellipse so there are infinite sides.")

# Object creation and methods calling
# Each class has a seperate object
# Methods are called for each class
Square_object = Square()
Square_object.calculateArea()
Square_object.calculatePerimeter()
Square_object.noofsides()

Rectangle_object = Rectangle()
Rectangle_object.calculateArea()
Rectangle_object.calculatePerimeter()      
Rectangle_object.noofsides()

Circle_object  = Circle()
Circle_object.calculateArea()
Circle_object.calculatePerimeter() 
Circle_object.noofsides()

Ellipse_object = Ellipse()
Ellipse_object.calculateArea()
Ellipse_object.calculatePerimeter() 
Ellipse_object.noofsides()

      
