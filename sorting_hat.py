'''
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin

Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

'''
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0


print("Do you like Dawn or Dusk?")

answer = int(input("Enter your answer (in numbers 1-2): "))

if answer == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
  print("Gryffindor and Ravenclaw both get a +1.")
elif answer == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
  print("Hufflepuff and Slytherin both get a +1.")
else:
  print("Wrong input")

print(" ")

print("When I’m dead, I want people to remember me as:")
answer = int(input("Enter your answer (in numbers 1-4): "))
if answer == 1:
  hufflepuff = hufflepuff + 2
  print("Hufflepuff +2.")
elif answer == 2:
  slytherin = slytherin + 2
  print("Slytherin +2.")
elif answer == 3:
  ravenclaw = ravenclaw + 2
  print("Ravenclaw +2.")
elif answer == 4:
  gryffindor = gryffindor + 2
  print("Gryffindor +2.")
else:
  print("Wrong input")

print(" ")
print("Which kind of instrument most pleases your ear?")
answer = int(input("Enter your answer (in numbers 1-4): "))
if answer == 1:
  slytherin = slytherin + 4
  print("Slytherin +4.")
elif answer == 2:
  hufflepuff = hufflepuff + 4
  print("Hufflepuff +4.")
elif answer == 3:
  ravenclaw = ravenclaw + 4
  print("Ravenclaw +4.")
elif answer == 4:
  gryffindor = gryffindor + 4
  print("Gryffindor +4.")
else:
  print("Wrong input")

print (" ")

print("Gryffindor: " + str(gryffindor))
print("Ravenclaw: " + str(ravenclaw))
print("Hufflepuff: " + str(hufflepuff))
print("Slytherin: " + str(slytherin))

print(" ")

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print(gryffindor)
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print(ravencw)
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print(hufflepuff)
else:
  print(slytherin)