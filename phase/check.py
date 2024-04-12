import phase.phase_constants as phase_constants


def end_game_choice():
    print("Do you really want to quit the game?")
    while True:
        print("0 - Back to the game")
        print("1 - End the game")
        endgame_choice = input("Back or End?")
        if endgame_choice not in [0, 1]:
            print("Invalid input")
            continue

        if endgame_choice == "0":
            return False
        elif endgame_choice == "1":
            return True


def phase_check(next_phase):
    while True:
        print("0 - Continue to FIGHT")
        print("1 - Edit hero")
        print("2 - Save the game")
        print("3 - End the game")
        menu_input = input("What you want to do?")

        if menu_input not in [0, 1, 2, 3]:
            print("Invalid input")
            continue

        if menu_input == 0:
            return next_phase
        elif menu_input == 1:
            # TODO hero check
            continue
        elif menu_input == 2:
            # TODO save game
            continue
        elif menu_input == 3:
            if end_game_choice():
                return phase_constants.END
