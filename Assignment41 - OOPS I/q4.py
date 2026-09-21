'''
Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8
'''


class Rectangle:

    def __init__(self,length,breadth):

        self.length = length
        self.breadth = breadth 

    def calculate_area(self):
        area = self.length*self.breadth

        return area

    def calculate_perimeter(self):
        perimeter = 2*(self.length+self.breadth)

        return perimeter

    def display(self):

        print(f"Length            :{self.length}")
        print(f"Breadth           :{self.breadth}")
        print(f"Area              :{self.calculate_area()}")
        print(f"Perimeter         :{self.calculate_perimeter()}")


length = int(input("Enter length : "))
breadth = int(input("Enter Breadth : "))

first = Rectangle(length,breadth)

first.display()
       