#inheritance = form new classes with the classes that have already been defined
# reuse code and reduce complexity of a program

#base class
class Animal():
   def __init__(self):
      print("animal created")
   
   def who_am_i(self):
      print("I am an animal")

   def eat(self):
      print("I am Eating")

# newly formed classes can use the animal class in order to inherit some of the methods you wanna use again

class Dog(Animal): #dog inherits animal
   def __init__(self):
      Animal.__init__(self)
      print("Dog Created")

   def bark(self):
      print("WOOF!")
   def eat(self):
      print("Dog is eating")

mydog = Dog()
mydog.eat()
mydog.bark()

# ==================
# Polymorphism
# refers to the way in which different object classes can share the same method name and then those methods can be called from the same place even tho a variety of objects might be passed in

class Dog():
   def __init__(self,name):
      self.name = name
   def speak(self):
      return self.name + " says woof!"
class Cat():
   def __init__(self,name):
      self.name = name
   def speak(self):
      return self.name + " says meow!"
niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
   print(type(pet))
   print(pet.speak())
# or
def pet_speak(pet):
   print(pet.speak())
pet_speak(niko)
#sharing the same method name "speak" and we can pass different objects

#-===================---========----==========----
#abstract classes in inheritance.
# abstract class = never expects to be instantiated to create an instance of the class and is only designed to serve as a base class

class Animal():
   def __init__(self,name):
      self.name = name
   def speak(self): # abstract method because in the base class itself, it isnt doing anything. It expects you to inherit the animal class and overrie the speak method
      raise NotImplementedError("Subclass must implement this abstract method")
myanimal = Animal('fred')

#instead what we expect you to do : :::: ---->>
class Dog(Animal):
   def speak(self):
      return self.name + " says woof!"
class Cat(Animal):
   def speak(self):
      return self.name + " says meow!"
fido = Dog('Fido')
isis = Cat('isis')
isis.speak()


# special methods 
#==========================================================

class Sample():
   pass
#mysample = Sample()
# len(mysample) #error
# print(mysample) #located output
# so how to use these funcs?

class Book():
   def __init__(self,title,author,pages):
      self.title = title
      self.author = author
      self.pages = pages
   
   def __str__(self):
      return f"{self.title} by {self.author}"
   def __len__(self):
      return 700
   def __del__(self):
      print("The book object is deleted.")
# the book object now has a special string representation of itself because of the str method
b = Book('Python', "Jose", 700)
print(b)
print(len(b))
del b