import random

# Variables
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

# Prompt for inputs
game_images = [rock, paper, scissors]
player_choice = int(
    input("Please select 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Output
    print(game_images[player_choice])
    computer_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_images[computer_choice])

    # Calculation
    if player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif computer_choice > player_choice:
        print("You lose.")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice == player_choice:
        print("It\'s a draw!")
