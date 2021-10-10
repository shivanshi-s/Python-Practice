# this is a guess the number game
import random
print('Hello there, What is your name ? ')
name = input()
theNumber = random.randint(1, 20)

print('Well, '+ name +' Im thinking of a number between 1 and 20, Can you guess what it is?')

#loop for number

for guessMade in range(1,7) : 
   print('Take a guess.')
   guess = int(input())

   if guess < theNumber : 
      print('Your guess is too low.')
   elif guess > theNumber : 
      print('Your guess is too high.')
   else : 
      break

if guess == theNumber:
   print('Ding Ding ' + name + '! You got it right! The number was indeed : '+ str(theNumber) + ' You took ' + str(guessMade) + ' guesses.')
else : 
   print('Oops, The number was '+ str(theNumber))
