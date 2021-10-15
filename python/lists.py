# list contains multiple items = [item1, item2, item3]
spam = [['cat','bat'], [10,20,30,40,50]]
print(spam[0])
print(spam[0][1]) #item inside the list   
print(spam[1])
print(spam[1][3])
print(spam[-1][-3])

#SLICE  : CAN GET SEVERAL VALUES FROM THE LIST
egs = ['rat','bat','cat','elephant']
print('The '+egs[-1]+ ' is afraid of the '+ egs[-2] )
print(egs[1:3]) #from 1 upto 3 but not including 3
egs[1:3] = ['THIS', 'IS', 'TAKEOVER']
print(egs)

print(list('Hello'))

#in and not in operators
print('howdy' in ['Hello','hi','howdy','heya']) #True

print('howdy' not in ['Hello','hi','howdy','heya']) #False