class Circle():
   def __init__(self,r):
      self.radius = r
   
   def area(self):
      print("Area of the circle is : ")
      return self.radius**2*3.14

   def perimeter(self):
      print("Perimeter of the circle is : ")
      return 2*3.14*self.radius

obj = Circle(3)
print(obj.area())
print(obj.perimeter())