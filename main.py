should_continue = True
while should_continue:
    print("Welcome in game called Arcadius\nDo you want play the game?")
    print("0 - Exit\n1- Play")

    intro_choice = int(input("What is your choice? "))
    if intro_choice not in [0, 1]:
        print("You have to choose between 0 and 1")
        continue

    if intro_choice == 0:
        print("Goodbye")
        should_continue = False
    elif intro_choice == 1:
        print("Welcome to the world of Arcadius")
        break
