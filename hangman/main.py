import random
import time
from hangman import hangman
from play_more import play_more

# Initial steps to invite in the game
print("Welcome to Hangman game!")
print("The game is about to start!\nLet's play Hangman!")
time.sleep(1)
print("You have 6 lives in each game! Choose letters carefully!")
another_hangman = True

while another_hangman:
    hangman()
    another_hangman = play_more()

print("Thank you for playing!")




