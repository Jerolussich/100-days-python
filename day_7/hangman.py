#!/usr/bin/python3

import random
import stages_hangman

# choose word and get length for findings print
word = ["word", "baboon", "camel"]
word_chosen = random.choice(word)
len_word = len(word_chosen)
counter = 0
current_fundings = []

#appends spaces to list and print
while counter < len_word:
    current_fundings.append("_ ")
    counter += 1
print(' '.join(current_fundings))


lifes_lost = 0

while lifes_lost < 5:

    # checks if no more letters need to be found
    if not("_ " in current_fundings):
            print("You win!!")
            break
    letter_guess = input("Guess a letter: ")

    positions = []

    for i, c in enumerate(word_chosen):
        if c == letter_guess:
            positions.append(i)
            current_fundings[i] = letter_guess

    if len(positions) == 0:
        print(stages_hangman.hangman_stages[lifes_lost])
        lifes_lost += 1

    if (lifes_lost == 5):
        print(stages_hangman.hangman_stages[5])
        print(f"The word was {word_chosen}")

    print(' '.join(current_fundings))


    
