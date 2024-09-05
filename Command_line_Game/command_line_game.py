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

name = input("Enter Your Name: ")
print("Welcome, " + name + ", to the land of adventure!")
print("You are standing in front of two doors. One is to the left and the other is to the right.")
choice = input("Which door do you want to choose? (left/right): ")

has_sword = False  # Flag to track whether the player has taken the sword

if choice == "left":
    print("You are in a room with no doors. It is empty.")
    choice2 = input("Do you want to stay here? (yes/no): ")
    if choice2 == "yes":
        print("You are still in the empty room.")
    elif choice2 == "no":
        print("You are back in front of the two doors.")
    else:
        print("Invalid choice. Please choose yes or no: ")
    
    choice3 = input("Do you want to look around? (yes/no): ")
    if choice3 == "yes":
        print("You see a sword on the ground.")
        choice4 = input("Do you want to take the sword? (yes/no): ")
        if choice4 == "yes":
            has_sword = True
            print("You took the sword!")
        else:
            print("You left the sword.")
    print("You return to the two doors.")
while choice != "right":
    choice= input("Now, you must choose the right door to proceed. (right): ")
if choice == "right":
    print("You are in a room with a dragon!")
    choice5 = input("Do you want to fight the dragon? (yes/no): ")
    if choice5 == "yes":
        if has_sword:
            print("You defeated the dragon and won the game!")
        else:
            print("You were eaten by the dragon and lost the game!")
    else:
        print("You chose not to fight the dragon and left the room.")

print("Thank you for playing!")
