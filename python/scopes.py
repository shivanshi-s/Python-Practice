spam =  42  #global scope

def eggs(): 
   spam = 41 #local variable local scope

print('Some code here.')  #global scope
print('Some code here.')


# 1. code in a global scope cannot use any local variables
# 2. Code in a local scope can access global variable
# 3. Code in one functions local scope cannot use vars in another funcs local scope
# 4. Same name for diff vars as long as in different scope
def spam() : 
   global eggs #even tho there is a global one we use the newer defined one
   eggs = 'Hello'
   print(eggs)

eggs = 43
spam()
print(eggs)