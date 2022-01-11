# Object oriented Programming!
#create code thats more reusable

class Dog():
   species = 'mammal'
   def __init__(self,breed,name): #constructor called automatically when an instance is created, self is instance of object itself
      # attribute (instance of the object) = parameter
      #we take in the atrribute and assign it using self.attribute_name
      self.breed = breed
      self.name = name
      # #expect boolean true/false
      # self.spots = spots
# methods - function inside a class 
   def bark(self,number):
      print("Woof! My name is {} and the number is {}".format(self.name,number)) #this particular instance, find the name , self.number not there bc user is providing that not conneccted to the instance of the class

my_dog = Dog('lab','Sammy')
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark(12)) #action
#methods use the info of the class 




# ==== attributes and methods= actions performed with the class
class Circle():
   #class object attribute
   pi = 3.14

   def __init__(self,radius=1):
      self.radius = radius
      self.area = radius * radius *Circle.pi # self.pi or circle.pi bc its a class object attribute

   # method
   def get_circumference(self):
      return self.radius * Circle.pi * 2

my_circle = Circle(22)
my_circle.pi
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)