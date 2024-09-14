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

def save_game(player_name, inventory, doors_chosen):
    """Saves the current game state to a file.
    
    Args:
        player_name (str): The name of the player.
        inventory (list): The list of items the player currently has.
        doors_chosen (dict): Dictionary indicating whether the left and right doors have been chosen.
    """
    with open('game_save.txt', 'w') as file:
        file.write(f"{player_name}\n")
        file.write(",".join(inventory) + "\n")
        file.write(f"{doors_chosen['left']},{doors_chosen['right']}\n")


def load_game():
    """Loads the game state from a file, if it exists.
    
    Returns:
        tuple: A tuple containing the player's name (str), inventory (list), and doors_chosen (dict).
    """
    try:
        with open('game_save.txt', 'r') as file:
            player_name = file.readline().strip()
            inventory = file.readline().strip().split(",") if file.readline().strip() else []
            doors_status = file.readline().strip().split(",")
            doors_chosen = {"left": doors_status[0] == "True", "right": doors_status[1] == "True"}
            return player_name, inventory, doors_chosen
    except FileNotFoundError:
        return None, [], {"left": False, "right": False}


def choose_door(doors_chosen, inventory):
    """Handles the player's choice of doors and updates the game state accordingly.
    
    Args:
        doors_chosen (dict): Dictionary tracking which doors have been chosen.
        inventory (list): The list of items the player currently has.
    
    Returns:
        tuple: Updated doors_chosen (dict) and inventory (list) after the player chooses a door.
    """
    available_doors = []
    if not doors_chosen["left"]:
        available_doors.append("left")
    if not doors_chosen["right"]:
        available_doors.append("right")
    
    print(f'{"You return to the two doors.":^30}')
    if available_doors:
        print(f'{"Available doors are: " + ", ".join(available_doors):^30}')
    
    choice = ""
    while choice not in available_doors:
        choice = input(f'{"Which door do you want to choose? (left/right): ":^30}').lower()

    if choice == "left" and not doors_chosen["left"]:
        print(f'{"You are in a room with no doors. It is empty.":^30}')
        if input(f'{"Do you want to look around? (yes/no): ":^30}').lower() == "yes":
            print(f'{"You see a sword on the ground.":^30}')
            if input(f'{"Do you want to take the sword? (yes/no): ":^30}').lower() == "yes":
                inventory.append("sword")
                print(f'{"You took the sword!":^30}')
            else:
                print(f'{"You left the sword.":^30}')
        doors_chosen["left"] = True

    elif choice == "right" and not doors_chosen["right"]:
        print(f'{"You enter a room and find a shield!":^30}')
        if input(f'{"Do you want to take the shield? (yes/no): ":^30}').lower() == "yes":
            inventory.append("shield")
            print(f'{"You took the shield!":^30}')
        else:
            print(f'{"You left the shield.":^30}')
        doors_chosen["right"] = True
    
    save_game(player_name, inventory, doors_chosen)  # Save progress after door choice
    return doors_chosen, inventory


def combat(choice, inventory):
    """Handles combat encounters with enemies based on player's choices and items.
    
    Args:
        choice (str): The enemy the player chooses to fight ("dragon" or "goblin").
        inventory (list): The player's current inventory of items.
    
    Returns:
        list: Updated inventory after the combat encounter.
    """
    if choice == "dragon":
        print(f'{"You enter a room with a fierce dragon!":^30}')
        if input(f'{"Do you want to fight the dragon? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                if random.randint(1, 6) > 3:
                    print(f'{"You defeated the dragon with your sword!":^30}')
                else:
                    if "shield" in inventory:
                        print(f'{"The dragon overpowered you, but your shield saved you!":^30}')
                        inventory.remove("shield")
                    else:
                        print(f'{"The dragon overpowered you and you lost the game!":^30}')
                        inventory.clear()
            else:
                print(f'{"You were eaten by the dragon because you had no sword!":^30}')
                inventory.clear()
    elif choice == "goblin":
        print(f'{"You enter a room with a sneaky goblin!":^30}')
        if input(f'{"Do you want to fight the goblin? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                if random.randint(1, 6) > 2:
                    print(f'{"You defeated the goblin with your sword!":^30}')
                else:
                    if "shield" in inventory:
                        print(f'{"The goblin tricked you, but your shield protected you!":^30}')
                        inventory.remove("shield")
                    else:
                        print(f'{"The goblin tricked you and you lost the game!":^30}')
                        inventory.clear()
            elif "shield" in inventory:
                print(f'{"The goblin attacked, but your shield saved you!":^30}')
                inventory.remove("shield")
            else:
                print(f'{"The goblin defeated you because you had no sword or shield!":^30}')
                inventory.clear()
    return inventory


def play_game():
    """Main function that runs the game logic."""
    global player_name
    player_name, inventory, doors_chosen = load_game()
    
    if not player_name:
        player_name = input(f"{'Enter Your Name: ':^30}")
        print(f"Welcome, {player_name}, to the land of adventure!")
    
    while not all(doors_chosen.values()):
        doors_chosen, inventory = choose_door(doors_chosen, inventory)
    
    print(f'{"You now see two more doors: one leads to a dragon, and the other to a goblin.":^30}')
    next_choice = input(f'{"Which door will you choose? (dragon/goblin): ":^30}').lower()
    inventory = combat(next_choice, inventory)
    
    if "sword" in inventory:
        print(f"Congratulations, {player_name}! You finished the game with a sword!")
    if "shield" in inventory:
        print(f"Congratulations, {player_name}! You finished the game with a shield!")
    if not inventory:
        print(f"Thank you for playing, {player_name}, but you lost all your items!")


# Start the game
play_game()