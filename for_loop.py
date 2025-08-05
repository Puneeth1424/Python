'''
To loop through a set of code a specified number of times, we can use a for loop and the range() function.

The range() function returns a sequence of numbers. By default, the sequence starts at 0 and increments by 1, ending at a specified number.
'''

for i in range(6):
  print(i)

'''
 this stops at 5, and 6 is not printed. This is because range() actually ends one before the specified number.
'''

for i in range(101):
  print("I will not use Snapchat in class" )
