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

index_count = 0
word = 'abcde'
for letter in word:
   print(word[index_count])
   index_count +=1
# what i could do instead of this -------:>>>>>>
# enumerate function  = take in any iterable object and returns index and the item
word = 'abcde'
for item in enumerate(word):
   print(item)

# ----- zip function - zips togerther 2 lists
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
   print(item)
# tuples of 2 items, zips as far as the values are same

# RANDOM LIBRARY
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist) 
#doesnt return anything and it is NONE type
from random import randint
randint(0,100)
print(randint(0, 100))

# LIST COMPREHENSIONS
mystring = 'hello'
mylist = []
for letter in mystring:
   mylist.append(letter)

# MORE EFFICIENT WAY  ====>
mylist = [letter for letter in mystring]
#---
mylist = [x for x in 'word' ]
#element for element in some iterable object
mylist = [num**2 for num in range(0,11)]

mylist =[x for x in range(0,11) if x%2 ==0]

celcius = [0,10,20,34.5]
fahrenheit = [ ( (9/5)*temp + 32 ) for temp in celcius]
print(fahrenheit)


