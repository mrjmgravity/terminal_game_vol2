INTRO_TEXT = "Welcome in game called Arcadius\nDo you want play the game?\n0 - Exit\n1 - Play"

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
    print(f"Is this your nickname {choose_name}? Or you want to change it\n0 - Change the nickname\n"
          f"1 - Confirm nickname ")
    name_choice = int(input("Your choice: "))
    if name_choice == 0:
        continue
    elif name_choice == 1:
        print(f"Hello {choose_name}, welcome in Arcadius.")
        break
