'''
Rock Paper Scissors
Pawelski
3/13/2023
Python II

Instructions:
Remove one of the pass keywords and try running the
program. What happens? What is the point of pass?
What does random.randint(1, 3) do?

Complete the program by replacing the passes. How
did the comments help you complete the program?

Rewrite the program so that it uses the logical
operator and.
'''

import random

player_choice = input("Rock, paper, or scissors? >> ")
computer_choice = random.randint(1, 3)
if computer_choice == 1: # computer picked rock
    if player_choice == "rock":
        print("It is a tie.")
    elif player_choice == "paper":
        print("The player won!")
    else:
        print("The computer won!")
elif computer_choice == 2: # computer picked paper
    if player_choice == "rock":
        pass
    elif player_choice == "paper":
        pass
    else:
        pass
else: # computer picked scissors
    pass