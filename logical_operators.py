'''
One more thing that we should learn is logical operators.

Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not operators:

and returns True if both conditions are True, and returns False otherwise.
or returns True if at least one of the conditions is True, and False otherwise.
not returns True if the condition is False, and vice versa.

'''
hunger = 0
anger = 2
coffee = 3
bubble_tea = 4
tired = 0

if hunger > 4 and anger > 1:
  print('Hangry')

if coffee > 0 or bubble_tea > 0:
  print('😊')

if not tired:
  print('Time to code!')

'''
They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

Create a new file called the_cyclone.py.

Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they have not met either requirement.

'''
height = int(input("Please enter your height: "))
credits = int(input("Please enter your credits: "))

if height >= 137 and credits >=10:
  print("Enjoy the ride")
elif height < 137 and credits == 10:
  print("You are not tall enough to ride.")
elif height >=137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("they have not met either requirement.")