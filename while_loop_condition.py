'''
A while loop looks very similar to an if statement. Just like an if statement, it executes the code if the condition is True.

However, the difference is that the while loop will continue to execute the code inside of it, over and over again, 
as long as the condition is True.

'''
guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))

'''
Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).

First, introduce a variable called tries at the top and give it a value of 0.

Then, add a second condition with the tries variable to the while loop using a relational operator.

'''
guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess !=6:
  print("you ran out of tries")
else:
  print("You got it")