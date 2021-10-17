# curly braces in key:value pairs
myCat = {'size':'fat',
         'color':'black',
         'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam = {
   12345: 'Luggage combination',
   42: 'The answer'
}
#items in dicts are UNORDERED
#in and not in operators work
# DICTONARIES ARE MUTABLE

# KEYS(), VALUES() AND ITEMS() ARE DICTIONARY METHODS

print(list(spam.keys()))
print((list(spam.values())))
print(list(spam.items()))

print(' ')

for k in myCat.keys():
   print(k)
print( ' ')
#GET() AND SETDEFAULT() METHODS

picnic = {'spoons':12, 'plates':4}
print('I am bringing ' + str(picnic.get('napkins',0)) + ' napkins to the picnic.')

print( ' ')
eggs = { 'name': 'Zophie', 'species':'cat', 'age': '5'}
eggs.setdefault('color','black')
print(eggs)