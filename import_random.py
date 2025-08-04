'''
We can use the .randint() function from a module called random to generate a random number from a range.

Next, we'll create a variable to store the randomly generated value. 
Declare a variable called num, and assign it to the function call:

This will generate a random number between 1 and 9 (inclusive of both).
The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...

'''

import random

num = random.randint(1, 9)

print(num)

'''
It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.

Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

'''

import random

question = input('Question:      ')

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Magic 8 Ball:  ' + answer)