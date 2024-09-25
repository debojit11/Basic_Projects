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
import requests
import os  # Used to check if the file exists

# Opponent base class
class Opponent:
    def __init__(self, name, health, attack_strength):
        self.name = name
        self.health = health
        self.attack_strength = attack_strength

    def attack(self):
        """General attack logic for opponents."""
        return random.randint(1, self.attack_strength)

# WeakOpponent class inheriting from Opponent
class WeakOpponent(Opponent):
    def __init__(self, name, health, attack_strength):
        super().__init__(name, health, attack_strength)

    def attack(self):
        """Overriding attack for weak opponents."""
        print(f"{self.name} attacks weakly!")
        return random.randint(1, self.attack_strength // 2)  # Weak attack is halved

# FinalBoss class inheriting from Opponent
class FinalBoss(Opponent):
    def __init__(self, name, health, attack_strength, special_power):
        super().__init__(name, health, attack_strength)
        self.special_power = special_power  # New attribute for FinalBoss

    def attack(self):
        """Overriding attack for final bosses with special power."""
        if random.random() > 0.7:  # 30% chance of using special power
            print(f"{self.name} uses {self.special_power}!")
            return random.randint(self.attack_strength, self.attack_strength * 2)
        else:
            print(f"{self.name} attacks normally.")
            return super().attack()

# Additional methods for game logic

def save_game(player_name, inventory, doors_chosen, current_language, translation_history):
    """Saves the current game state to a file."""
    with open('game_save.txt', 'w') as file:
        file.write(f"{player_name}\n")
        file.write(",".join(inventory) + "\n")
        file.write(f"{doors_chosen['left']},{doors_chosen['right']}\n")
        file.write(f"{current_language}\n")
        file.write(f"{translation_history['from']},{translation_history['to']}\n")

def load_game():
    """Loads the game state from a file if it exists."""
    if not os.path.exists('game_save.txt'):
        return None, [], {"left": False, "right": False}, "en", {"from": "en", "to": "en"}

    with open('game_save.txt', 'r') as file:
        file_content = file.readlines()

    player_name = file_content[0].strip()
    inventory = file_content[1].strip().split(",") if file_content[1].strip() else []
    doors_status = file_content[2].strip().split(",")
    doors_chosen = {"left": doors_status[0] == "True", "right": doors_status[1] == "True"}
    current_language = file_content[3].strip()
    translation_history = dict(zip(["from", "to"], file_content[4].strip().split(",")))

    return player_name, inventory, doors_chosen, current_language, translation_history

def get_random_name(min_len=2, max_len=40):
    """Gets a random name from Uzby API."""
    url = f"https://uzby.com/api.php?min={min_len}&max={max_len}"
    response = requests.get(url)
    return response.text

def translate_text(text, source_lang, target_lang):
    """Translates text using LibreTranslate API."""
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }
    response = requests.post(url, data=payload)
    return response.json()['translatedText']

def choose_door(doors_chosen, inventory):
    """Handles the player's choice of doors and updates the game state accordingly."""
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
    
    save_game(player_name, inventory, doors_chosen, current_language, translation_history)
    return doors_chosen, inventory

def combat(choice, inventory):
    """Handles combat encounters using the new Opponent system."""
    if choice == "dragon":
        dragon = FinalBoss("Dragon", health=100, attack_strength=20, special_power="Fire Breath")
        print(f'{"You encounter a fearsome dragon!":^30}')
        if input(f'{"Do you want to fight the dragon? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                player_attack = random.randint(1, 10)  # Simulating player's attack
                dragon_attack = dragon.attack()

                if player_attack >= dragon_attack:
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
        goblin = WeakOpponent("Goblin", health=50, attack_strength=5)
        print(f'{"You encounter a sneaky goblin!":^30}')
        if input(f'{"Do you want to fight the goblin? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                player_attack = random.randint(1, 10)  # Simulating player's attack
                goblin_attack = goblin.attack()

                if player_attack >= goblin_attack:
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
    player_name, inventory, doors_chosen, current_language, translation_history = load_game()

    if not player_name:
        player_name = input("Enter your name: ")

    print(f'{"Welcome to the Adventure Game, " + player_name + "!":^30}')
    
    # Let player choose a door
    doors_chosen, inventory = choose_door(doors_chosen, inventory)

    # Encounter either a goblin or a dragon randomly
    encounter = random.choice(["goblin", "dragon"])
    inventory = combat(encounter, inventory)

if __name__ == "__main__":
    play_game()