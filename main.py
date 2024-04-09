INTRO_TEXT = "Welcome in game called Arcadius\nDo you want play the game?\n0 - Exit\n1 - Play"

abilities = {
    "Attack damage": {
        "points": 1,
        "description": "Attack damage is important with base attack and its connected with Dexterity and Luck"
    },
    "Defense": {
        "points": 1,
        "description": "Celkový obrana sa ráta z bodov obrany + obratnosti."
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

should_continue = True
while should_continue:
    print(INTRO_TEXT)

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

is_name = True
while is_name:
    choose_name = input("What is your nickname? ")
    print(f"Is this your nickname {choose_name}? Do you want to change it?\n0 - Change the nickname\n"
          f"1 - Confirm nickname ")
    name_choice = int(input("Your choice: "))
    if name_choice == 0:
        continue
    elif name_choice == 1:
        print(f"Hello {choose_name}, welcome in Arcadius.")
        break
    else:
        print("Invalid choice")
        continue
