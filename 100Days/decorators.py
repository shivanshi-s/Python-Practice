# decorators
# Allow you to "decorate" a function
# Decorators allow you to tack on extra functionality to an already existing function and no longer want it- delete one line from the decorator
# @ some_decorator
# manually building this =====>

def hello(name="jose"):
   print("The hello() func has been executed")
   
   def greet():
      return '\t This is the greet() func inside hello!'

   def welcome():
      return '\t This is welcome() func inside hello!'
   
   print("I am going to return a function")
   if name == "jose":
      return greet
   else:
      return welcome

myfunc = hello()
print(myfunc())


# =======
# return functions and execute them when assigned to a variable
def cool():
   def supercool():
      return 'I am v cool'
   return supercool

somefunc = cool()
print(somefunc)
print(somefunc())

# =======
# how we can pass in functions into another function
def hello():
   return 'Hi Jose!'

def other(some_def):
   print("Other code runs here!")
   print(some_def())

other(hello)

# =========== decorators
def new_decorator(original_func):

   def wrap_func():
      print("some extra code, before the original func")

      original_func()

      print("some extra code, after the original function")

   return wrap_func

def func_needs_decorator():
   print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator) # this has a special syntax
decorated_func()


# sepcial syntax : 
@new_decorator # this is your on/off switch
def func_needs_decorator():
   print("I want to be decorated!")

func_needs_decorator()