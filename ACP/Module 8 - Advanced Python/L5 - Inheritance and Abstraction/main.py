#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Shape(ABC):

    #abstract method
        #should be implemented by all sub-classes
        def area(self):
            pass

    #sub classes
class Triangle(Shape):

    def area(self):
        print("A = bh/2")

class Quadrilateral(Shape):

    def area(self):
        print('A = bh')

class Trapezoid(Shape):
        
    def area(self):
        print("A = ((b1+b2)/2)h")

class Circle(Shape):
     def area(self):
          print('A = πr^2')
#Driver code
R = Triangle()
R.area()

K = Quadrilateral()
K.area()

R = Trapezoid()
R.area()

K = Circle()
K.area()
