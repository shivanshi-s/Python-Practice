# lets talk about lists and tuples as data types in python
# Lists are ordered sequences that can hold a variety of object trypes.

# support - indexeing and slicing  -- can be nested and lots of methods 


my_list = [1,2,3] # basic list 
my_list  = ['String',100,23.2]
len(my_list)

mylist = ['one','two','three']
mylist[0] #one
mylist[1:]#['two, three]

#concatenate two lists
another_list = ['four','five']
new_list = my_list + another_list

#changing elements in a list
#MUTABLE UNLIKE STRINGS

new_list[0] = 'ONE ALL CAPS'
print(new_list)

#affecting in place - APPEND - add to the end of the list
new_list.append('six')

#removing items from the list POP
new_list.pop() #six
print(new_list)

# at  a specific index -
new_list.pop(0)
print(new_list)

# SORT AND REVERSE

new_list = ['a','b','x','b','c']
num_list = [4,1,8,3]
new_list.sort() #doesnt return anything so u cant assign

# None = indicate no value - return value for functions that donot return anything.

num_list.reverse()

# ------------------------------------------
#tuple - for coordinates, hold information
#KEY DIFFERENCE = IMMUTABLE  - CANNOT BE CHANGED
position = (2,'Hello')
color = (255,255,255)
print(type(color))

t = ('one',2,3)
mylist = [1,2,3]
len(t)

t[0] #one

t = ('a','b','c')
t.count('a') # all the index locations a occurs
t.index('a') # the very first time it appears in the index

#immutability ==========

mylist[0] = 'NEW'
print(mylist)
t[0] = 'NEW' #error

# why use tuples --------> passing objects making sure they dont get changed ----- DATA INTEGRITY 

