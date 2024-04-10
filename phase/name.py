import phase.phase_constants


def name_phase():
    while True:
        choose_name = input("What is your nickname? ")
        print(f"Is this your nickname {choose_name}? Do you want to change it?\n0 - Change the nickname\n"
              f"1 - Confirm nickname ")
        try:
            name_choice = int(input("Your choice: "))
            if name_choice == 0:
                continue
            elif name_choice == 1:
                print(f"Hello {choose_name}, welcome in Arcadius.")
                return phase.phase_constants.INTRO_ABILITIES
            else:
                print("Invalid choice")
                continue
        except ValueError:
            print("Please enter number")

