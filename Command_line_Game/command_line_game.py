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

import random

# Game setup
name = input(f"{'Enter Your Name: ':^30}")
print(f"Welcome, {name}, to the land of adventure!")

# Player's inventory
inventory = []

# Track which doors have been chosen
doors_chosen = {"left": False, "right": False}

# Let the player choose a door while avoiding previously chosen doors
while not all(doors_chosen.values()):  # Loop until both doors have been chosen
    available_doors = []
    if not doors_chosen["left"]:
        available_doors.append("left")
    if not doors_chosen["right"]:
        available_doors.append("right")
    
    print(f'{"You return to the two doors.":^30}')
    if available_doors:
        print(f'{"Available doors are: " + ", ".join(available_doors):^30}')
    
    # Prompt player to choose an available door
    choice = ""
    while choice not in available_doors:
        choice = input(f'{"Which door do you want to choose? (left/right): ":^30}').lower()

    if choice == "left" and not doors_chosen["left"]:
        print(f'{"You are in a room with no doors. It is empty.":^30}')
        choice2 = input(f'{"Do you want to look around? (yes/no): ":^30}').lower()
        
        if choice2 == "yes":
            print(f'{"You see a sword on the ground.":^30}')
            take_sword = input(f'{"Do you want to take the sword? (yes/no): ":^30}').lower()
            if take_sword == "yes":
                inventory.append("sword")
                print(f'{"You took the sword!":^30}')
            else:
                print(f'{"You left the sword.":^30}')
        doors_chosen["left"] = True  # Mark the left door as chosen
    
    elif choice == "right" and not doors_chosen["right"]:
        print(f'{"You enter a room and find a shield!":^30}')
        take_shield = input(f'{"Do you want to take the shield? (yes/no): ":^30}').lower()
        if take_shield == "yes":
            inventory.append("shield")
            print(f'{"You took the shield!":^30}')
        else:
            print(f'{"You left the shield.":^30}')
        doors_chosen["right"] = True  # Mark the right door as chosen

# Now, proceed to the next challenge after exploring both rooms
print(f'{"You now see two more doors: one leads to a dragon, and the other to a goblin.":^30}')
next_choice = input(f'{"Which door will you choose? (dragon/goblin): ":^30}').lower()

# Dragon room logic
if next_choice == "dragon":
    print(f'{"You enter a room with a fierce dragon!":^30}')
    fight_dragon = input(f'{"Do you want to fight the dragon? (yes/no): ":^30}').lower()
    
    if fight_dragon == "yes":
        if "sword" in inventory:
            print(f'{"Rolling the dice to see the outcome...":^30}')
            dice_result = random.randint(1, 6)
            if dice_result > 3:  # Higher chance of winning with a sword
                print(f'{"You defeated the dragon with your sword!":^30}')
            else:
                if "shield" in inventory:
                    print(f'{"The dragon overpowered you, but your shield saved you!":^30}')
                    inventory.remove("shield")  # Lose shield after blocking
                else:
                    print(f'{"The dragon overpowered you and you lost the game!":^30}')
                    inventory.clear()  # Lose everything if defeated without shield
        else:
            print(f'{"You were eaten by the dragon because you had no sword!":^30}')
            print(f'{"You lost all items in your inventory!":^30}')
            inventory.clear()

# Goblin room logic
elif next_choice == "goblin":
    print(f'{"You enter a room with a sneaky goblin!":^30}')
    fight_goblin = input(f'{"Do you want to fight the goblin? (yes/no): ":^30}').lower()
    
    if fight_goblin == "yes":
        if "sword" in inventory:
            print(f'{"Rolling the dice to see the outcome...":^30}')
            dice_result = random.randint(1, 6)
            if dice_result > 2:  # Easier to defeat the goblin
                print(f'{"You defeated the goblin with your sword!":^30}')
            else:
                if "shield" in inventory:
                    print(f'{"The goblin tricked you, but your shield protected you!":^30}')
                    inventory.remove("shield")  # Lose shield after blocking
                else:
                    print(f'{"The goblin tricked you and you lost the game!":^30}')
                    inventory.clear()
        elif "shield" in inventory:
            print(f'{"The goblin attacked, but your shield saved you!":^30}')
            inventory.remove("shield")  # Lose shield after blocking
        else:
            print(f'{"The goblin defeated you because you had no sword or shield!":^30}')
            inventory.clear()

# End of the game
if "sword" in inventory:
    print(f"Congratulations, {name}! You finished the game with a sword!")
if "shield" in inventory:
    print(f"Congratulations, {name}! You finished the game with a shield!")
if not inventory:
    print(f"Thank you for playing, {name}, but you lost all your items!")

