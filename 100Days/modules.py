from collections import Counter

mylist = [1,2,3,4,5,6,6,7,7,7,4,4,6,6,9]
print(Counter(mylist))
# counter is a dictionary subclass

print(Counter('aaab'))

# =================
# opening and reading files on the computer

# f = open('practice.txt', 'w+')
# f.write('this is a text string')
# f.close()
import os
print(os.getcwd()) #get current worsking directory
print(os.listdir()) # files inside the directory

