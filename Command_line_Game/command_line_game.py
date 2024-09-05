#Ask the player for their name.
#Display a message that greets them and introduces them to the game world.
#Present them with a choice between two doors.
#If they choose the left door, they'll see an empty room.
#If they choose the right door, then they encounter a dragon.
#In both cases, they have the option to return to the previous room or interact further.
#When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
#When encountering the dragon, they have the choice to fight it.
#If they have the sword from the other room, then they will be able to defeat it and win the game.
#If they don't have the sword, then they will be eaten by the dragon and lose the game.

name = input(f"{'Enter Your Name: ':^30}")
print("Welcome, " + name + ", to the land of adventure!")
print("You are standing in front of two doors. One is to the left and the other is to the right.")
choice = input(f'{"Which door do you want to choose? (left/right): ":^30}')

has_sword = False  # Flag to track whether the player has taken the sword

if choice == "left":
    print(f'{"You are in a room with no doors. It is empty.":^30}')
    choice2 = input(f'{"Do you want to stay here? (yes/no): ":^30}')
    if choice2 == "yes":
        print(f'{"You are still in the empty room.":^30}')
    elif choice2 == "no":
        print(f'{"You are back in front of the two doors.":^30}')
    else:
        print(f'{"Invalid choice. Please choose yes or no: ":^30}')
    
    choice3 = input(f'{"Do you want to look around? (yes/no): ":^30}')
    if choice3 == "yes":
        print(f'{"You see a sword on the ground.":^30}')
        choice4 = input(f'{"Do you want to take the sword? (yes/no): ":^30}')
        if choice4 == "yes":
            has_sword = True
            print(f'{"You took the sword!":^30}')
        else:
            print(f'{"You left the sword.":^30}')
    print(f'{"You return to the two doors.":^30}')
while choice != "right":
    choice= input(f'{"Now, you must choose the right door to proceed. (right): ":^30}')
if choice == "right":
    print(f'{"You are in a room with a dragon!":^30}')
    choice5 = input(f'{"Do you want to fight the dragon? (yes/no): ":^30}')
    if choice5 == "yes":
        if has_sword:
            print(f'{"You defeated the dragon and won the game!":^30}')
        else:
            print(f'{"You were eaten by the dragon and lost the game!":^30}')
    else:
        print(f'{"You chose not to fight the dragon and left the room.":^30}')

print(f'{"Thank you for playing!":^30}')
