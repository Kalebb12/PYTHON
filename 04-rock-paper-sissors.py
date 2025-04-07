rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇
choices = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
aiChoice = random.randint(0, 2)
if userChoice >= 3 or userChoice < 0:
    print("You chose an invalid number, you lose")
    exit()
if userChoice == 0 and aiChoice == 2:
    result = "win"
elif userChoice == 0 and aiChoice == 1:
    result = "lose"
elif userChoice == 1 and aiChoice == 0:
    result = "win"
elif userChoice == 1 and aiChoice == 2:
    result = "lose"
elif userChoice == 2 and aiChoice == 0:
    result = "lose"
elif userChoice == 2 and aiChoice == 1:
    result = "win"
elif userChoice == aiChoice:
    result = "draw"
print(f"{choices[userChoice]}\ncomputer chose:\n{choices[aiChoice]}\nYou {result}")