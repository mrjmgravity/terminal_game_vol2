import phase.phase_constants


INTRO_TEXT = "Welcome in game called Arcadius\nDo you want play the game?\n0 - Exit\n1 - Play"


def intro_phase():
    while True:
        print(INTRO_TEXT)
        try:
            intro_choice = int(input("What is your choice? "))
            if intro_choice not in [0, 1]:
                print("You have to choose between 0 and 1")
                continue

            if intro_choice == 0:
                print("Goodbye")
                return phase.phase_constants.END
            elif intro_choice == 1:
                print("Perfect, introduce yourself")
                return phase.phase_constants.NAME
        except ValueError:
            print("Please enter number")
