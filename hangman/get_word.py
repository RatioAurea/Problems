import random

def get_word():
    words_to_guess = []
    with open("words", "r") as file:
        for line in file:
            words_to_guess.append(line.rstrip('\n'))

    word = random.choice(words_to_guess)

    return word