#equality
2 == 2
2 == 1
'hello' == 'bye'
'Bye' == 'bye' #false
2.0 == 2 #true
2 > 1 #true

# chaining comparison operators
# use of logical operators - and , or , not

('h' == 'h') and (2 == 2) # is left and right both true?
100 == 1 or 2 == 2 # one of them to be true

not 1 == 1 #false

# --------------------------------------------------------
# ---------------------------------------------------------
hungry  = False

if hungry:
   print('FEED ME!')
else:
   print('iM NOT HUNGRY')

#==================#

loc ='Bank'
if loc == 'Auto Shop':
   print('Cars are cool!')
elif loc == 'Bank':
   print('Money is cool!')
else:
   print('I do not know much.')

#=====================================

mylist = [1,2,3]
for num in range(0,11,2):
   print(num)
#range is a generator = func that generate info instead of saving it all to memory
list(range(0,11,2))


