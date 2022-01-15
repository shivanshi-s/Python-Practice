# GENERATORS
# ==== allow us to write a function that can send back a value and then later resume to pick up where it left off. ===
# generate a sewuence of values over time
# adv = generator computes one value waits until the next value is called for
# eg = range() func doesnt produce an list in memory for all the vals instead it keeps track of the last number and the step size, to provide a steady flow of numbers
# if a user did need that list = transform the generator list with list(range(0,100))

def create_cubes(n):
   result = []
   for x in range(n):
      result.append(x**3)
   return result
# print(create_cubes(10)) # this just created a agiant list in memory
# so instead we will yield it out

def create_cubes(n):
   for x in range(n):
      yield x**3

for x in create_cubes(4): # this is a generator, need to iterate through it to see the result
   print(x)
# create_cubes is now much more memory efficient

# ========== fibonacci sequence ============

def gen_fib(n):
   a = 1
   b = 1
   for i in range(n):
      yield a
      a,b = b,a+b

for number in gen_fib(10):
   print(number)

s = 'hello'
s_iter = iter(s) # changed into iteratorable string
print(next(s_iter))