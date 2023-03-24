def play_more():

    another_game = True
    answer = input("Do you want to play more? y = yes, n = no: ")
    while answer not in ["y", "n"]:
        answer = input("Invalid input. Do you want to play more? y = yes, n = no: ")

    if answer.lower() == "n":
        another_game = False

    return another_game