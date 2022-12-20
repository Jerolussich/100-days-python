#!/usr/bin/python3
import random

player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
random_number = random.randrange(0, 2)
rock = ('''
        _____
    ---' ____)
        (_____)
        (_____)
        (____)
    ---_(___)
    ''')
paper = ('''
         _______
    ---'    ____)____
              ______)
              _______)
            _______)
    ---.__________)
    ''')
scissors = (('''
        _______
    ---'   ____)____
            ________)
       __________)
      (____)
---.__(___)
    '''))
game_images = [rock, paper, scissors]
print(game_images[player_move])
print("Computer choose:\n")
print(game_images[random_number])
if(player_move == random_number):
        print("It's a draw")
if(player_move == 0):
    if (random_number == 1):
        print("You lose!")
    elif (random_number == 2):
        print("You win!")
if(player_move == 1):
    if (random_number == 0):
        print("You win!")
    elif (random_number == 2):
        print("You lose!")
if(player_move == 2):
    if (random_number == 0):
        print("You lose!")
    elif (random_number == 1):
        print("You win!")
    