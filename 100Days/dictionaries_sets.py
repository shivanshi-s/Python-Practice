# DICTIONARIES = unordered mappings for storing objects.
# KEY - VALUE PAIR = grab objects w/o knowing index location

# when to choose dictionary or when to choose a list?
# dicts - objects retrieved by key name, unordered and can not be sorted

# lists = objects retrieved by location, ordered and can be indexed or sliced.

#-----------------------

my_dict = { 'key1':'value1','key2':'value2'}
print(my_dict)
my_dict['key1']
#usecase - prices in a store

price_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
price_lookup['apple']

d = {'k1':123 , 'k2':[0,1,2], 'k3':{'insidekey':100}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insidekey'])
print(d['k2'][2])
#stacking calls 
print("------------------------")
d = {'key1':['a','b','c']}
print(d['key1'][2].upper())

d.keys()
d.values()
d.items() #pairs in tuples

#-------------------------------------------------------

#------setsssssssss-------------
#sets - unordered collections of unique elements
#  one representative of the same object

myset = set()
myset.add(1)
myset.add(2)
myset.add(2) # no repetition of the value
print(myset)
#only accepts unique vals

#casting list to a set
mylist = [1,1,1,2,3,4,2,3,4]
set(mylist) #unordered
