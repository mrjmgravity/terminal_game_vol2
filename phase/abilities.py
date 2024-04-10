from utility import print_abilities_options, print_abilities_points
from hero_data import abilities


def abilities_update():
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
