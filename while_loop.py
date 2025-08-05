'''
You can think of the while loop like a traffic circle.

Each lap is one iteration! A car will iterate over and over again until it can't do so anymore.

'''

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')