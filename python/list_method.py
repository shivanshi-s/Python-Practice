# list methods 
# method is attached on a certain value but is similar to function

spam = [ 'hello' , 'hi' , 'howdy', 'heya']
# list values have a method called index
print(spam.index('hello'))

# INDEX is a method called ON a value spam
# each data type has its own set of methods 
spam.append('bye')
print(spam)
spam.insert(1, 'Welcome')
print(spam)
#methods belong to a single data type - index, append , insert can only be called on list
spam.remove('howdy')
print(spam)

sp = ['cat', 'mat', 'rat', 'aaa', 'bbb']
sp.sort()
print(sp)
sp.sort(reverse=True)
print(sp)
# cant sort a list that has numbers and values
#ASCII - BETTICAL order
spamm = ['Alice', 'ali', 'Bob', 'Zero', 'cat']
spamm.sort()
print(spamm)
spamm.sort(key=str.lower)
print(spamm)

print(' ')

# lists and strings
# mutable and immutable data types
# lists are mutable - references any change changes the actual list  

import copy

color = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(color)
cheese[1] = 42
print(cheese)
print(' ')
print(color)

# the \ line continuation character can be used to stretch python instructions
# along multiple lines