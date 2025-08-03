import random

player = 0
computer = 0

player = int(input("Select a number between 1 and 3: "))

if player == 1:
    print("rock")
elif player == 2:
    print("paper")
elif player == 3:
    print("scissors")
else:
    print("Invalid")

computer = random.randint(1,3)

if computer == 1:
    print("rock")
elif computer == 2:
    print("paper")
elif computer == 3:
    print("scissors")
else:
    print("Invalid")

if player == computer:
    print("It's a tie")
elif player == 1 and computer == 3:
    print("Player won")
elif player == 1 and computer == 2:
    print("Computer won")
elif player == 2 and computer == 1:
    print("Player won")
elif player == 2 and computer == 3:
    print("Computer won")
elif player == 3 and computer == 1:
    print("Computer won")
elif player == 3 and computer == 2:
    print("Player won")
else:
    print("nothing")