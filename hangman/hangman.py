from get_word import get_word

def hangman():

    my_word = get_word()

    display = "_" * (len(my_word))
    print(display)
    counter = 0
    used_letters = []

    while "_" in display and counter < 6:
        lives_left = 6 - counter

        if lives_left == 1:
            guess = input(f"Enter your guess ({lives_left} life left): ").upper()
        else:
            guess = input(f"Enter your guess ({lives_left} lives left): ").upper()

        while guess not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                         "T", "U", "V", "W", "X", "Y", "Z"] or guess in used_letters:
            guess = input("Invalid input/already tried, try again: ").upper()

        used_letters.append(guess)
        print(f"Used letters: {used_letters}")

        help_word = ""
        not_guessed = True
        for i in range(0, len(my_word)):
            if my_word[i].upper() == guess:
                help_word = help_word + guess
                not_guessed = False
            else:
                help_word = help_word + display[i]

        if not_guessed:
            counter = counter + 1

        display = help_word
        print(display)

    if counter < 6:
        print(f"Congratulations, the word was '{my_word.upper()}'!")

    elif counter >= 6:
        print(f"You have no more lives! You lost! The word was '{my_word.upper()}'.")
