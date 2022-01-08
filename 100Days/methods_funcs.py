# methods and functions
''' methods are built in objects  '''
mylist = [1,2,3]
mylist.append(4)

help(mylist.index)
# functions allow us to create blocks of code that can be easily excuted many times

def name_of_function():
   ''' doctring explains function'''
   print('hello')

# ===========================================================
def say_hello(name):
   print(f'hello {name}')
say_hello('Jose')

#=======================================================
#tuple unpacking
stock_prices =[('APL,200'),('GOOG',400),('MSFT',100)]
for ticker,price in stock_prices:
   print(price(0.1*price))

work_hours=[('Abby',100),('Billy',4000),('Cassie',800)]
def employee_check(work_hours):

   current_max = 0
   employee_of_month = ''
   for employee,hours in work_hours:
      if hours > current_max:
         current_max = hours
         employee_of_month = employee
      else:
         pass

   #return
   return (employee_of_month,current_max)
print(employee_check(work_hours))

# ===========================================================

# --- *args and **kwargs
def myfunc(a,b,c=0,d=0):
   # returns 5% of the sum of a and b
   return sum((a,b)) * 0.05
print(myfunc(40, 60))

# star *args = arbitrary number of arguments

def myfunc(*args):
   return sum(args) * 0.05
print(myfunc(40,60,100,2,2,4,5,6)) #any number of args
# args - looks like a tuple

#------------------------------------
# **kwargs - keyworded arguments - builds a dictionary of key-value pairs

def myfunc(**kwargs):
   print(kwargs)
   if 'fruit' in kwargs:
      print('My fruit of choice is {}'.format(kwargs['fruit']))
   else:
      print('I did not find any fruit here')

print(myfunc(fruit='apple',veggie='lettuce'))

# =================================================
#lambda, map and filter
def square(num):
   return num**2
my_numes = [1,2,3,4,5,6]
for item in map(square,my_nums):
   print(item)


def splicer(mystring):
   if len(mystring)%2 == 0:
      return 'EVEN'
   else:
      return mystring[0]
names = ['Andy','Eve','Rachel']
list(map(slicer, names)) # function is passed as an argument here without the () because the map will later on execute them otherwise it will give error. We wanna pass the func, not execute it

def check_even(num):
   return num%2 == 0
mynums = [1,2,3,4,5,6]
list(filter(check_even, mynums))
#or 
for n in filter(check_even, mynums):
   print(n)

#=================================================

#LAMBDA
def square(num): return num ** 2

# labda -anonymous function= a function u only intend to use one time so thats why u dont give it a name or the def ekyword
square  = lambda num: num ** 2
print(square(5))
# used in conjunctions mainly
#with map funvtion
list(map(lambda num:num**2,mynums))
#with filter function
list(filter(lambda num:num%2 ==0,mynums))

names = ['Andy','Eve']
list(map(lambda x:x[::-1],names))

# ==========================================================
# NESTED FUNCS AND SCOPES

''' LEGB RULES: 
   L - local
   E - enclosing function locals
   G - global namespace
   B - Built-in 
'''
#global
name ='This is a global string'
def greet():
   #enclosing
   name = 'Sammy'

   def hello():
      #local
      name = 'Sally'
      print('Hello '+ name)
   hello()
print(greet())