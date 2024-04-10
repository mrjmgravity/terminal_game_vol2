INTRO_TEXT = "Welcome in game called Arcadius\nDo you want play the game?\n0 - Exit\n1 - Play"

abilities = {
    "Attack damage": {
        "points": 1,
        "description": "Attack damage is important with base attack and its connected with Dexterity and Luck"
    },
    "Defense": {
        "points": 1,
        "description": "Defense is calculating defense + dexterity."
    },
    "Dexterity": {
        "points": 1,
        "description": "Dexterity is important with defense and attack."
    },
    "Skill": {
        "points": 1,
        "description": "SKill is important with base attack and with critical strike."
    },
    "Health": {
        "points": 50,
        "description": "Health can be restored after battle."
    },
    "Luck": {
        "points": 1,
        "description": "Luck is important for critical strike."
    }
}


def print_abilities_options():
    for i, ability in enumerate(abilities.keys()):
        ability_option = str(i + 1) + ' - ' + ability
        if ability == "Život":
            ability_option += " " + "- jeden bod pridá 5 života"
        print(ability_option)


def print_abilities_points():
    for k, v in abilities.items():
        print(k + " - " + str(v["points"]), end=", ")
    print("\n")


should_continue = True
while should_continue:
    print(INTRO_TEXT)
    try:
        intro_choice = int(input("What is your choice? "))
        if intro_choice not in [0, 1]:
            print("You have to choose between 0 and 1")
            continue

        if intro_choice == 0:
            print("Goodbye")
            should_continue = False
        elif intro_choice == 1:
            print("Perfect, introduce yourself")
            break
    except ValueError:
        print("Please enter number")

is_name = True
while is_name:
    choose_name = input("What is your nickname? ")
    print(f"Is this your nickname {choose_name}? Do you want to change it?\n0 - Change the nickname\n"
          f"1 - Confirm nickname ")
    try:
        name_choice = int(input("Your choice: "))
        if name_choice == 0:
            continue
        elif name_choice == 1:
            print(f"Hello {choose_name}, welcome in Arcadius.")
            is_name = False
        else:
            print("Invalid choice")
            continue
    except ValueError:
        print("Please enter number")

    print("This is your abilities: ")
    print_abilities_points()

    abilities_picked = False
    ability_picked_count = 0
    while not abilities_picked:
        print_abilities_options()
        ability_choice = int(input("You have " + str(7 - ability_picked_count) + " points to assign: "))

        if ability_choice.is_integer() and int(ability_choice) in list(range(1, len(abilities) + 1)):
            chosen_ability_name = list(abilities.keys())[int(ability_choice) - 1]
            chosen_ability = abilities[chosen_ability_name]
        else:
            print("invalid input")
            continue

        if chosen_ability_name == "Health":
            chosen_ability["points"] += 5
        else:
            chosen_ability["points"] += 1

        print_abilities_points()

        ability_picked_count += 1
        if ability_picked_count == 7:
            abilities_picked = True
