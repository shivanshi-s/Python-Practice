print('Say hi to Bob\'s cat!')
print(r'This is carol\'s cat.') # raw string
print("""Dear Alice,
Eve's Cat has been arrested for catsortion, catnapping and cat burglary
Sincerely, Bob. """)


spam = 'Hello World'

#indexes, slices, negative indexes, in and not in operators, case sensitive - kinda like lists.
print('-------------------\n-------------------')

# ------------------ STRING METHODS -------------------------------

#string methods return new string values rather than modifying the string in place.
# since strings are IMMUTABLE- cannot be modified anyway

#upper, lower

spam = "hello world"
print(spam.upper())

print('Hello there'.startswith('hello'))

print(','.join(['cats','rats','mats']))

print('My name is Simon.'.split())

print('Hello'.rjust(10))
print('hello'.ljust(10,'*'))
print('Hello'.center(20,'='))

print('\n')

spam = "This is amazing"
print(spam.replace('i', 'X1Z'))

print('\n')

import pyperclip
pyperclip.copy('Helloooo!')
print(pyperclip.paste())


#=================== conversion specifiers ==========================

name = 'Alice'
place = 'my house'
time = '7pm'
food = 'pizza'

print('Hello %s, you are invited to a party at %s at %s please bring %s . ' % (name, place,time,food) )