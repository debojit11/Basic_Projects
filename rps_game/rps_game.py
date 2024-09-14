import random

def get_hand(hand):
    """
    Returns the string representation of the hand based on the input number.

    Args:
        hand (int): Number representing a hand (0 for Scissors, 1 for Rock, 2 for Paper)

    Returns:
        str: String representation of the hand.
    """
    hands = ['Scissors', 'Rock', 'Paper']
    return hands[hand]

def determine_winner(player_hand, computer_hand):
    """
    Determines the winner based on the player's and computer's hands.

    Args:
        player_hand (int): The player's hand (0 = Scissors, 1 = Rock, 2 = Paper).
        computer_hand (int): The computer's hand (0 = Scissors, 1 = Rock, 2 = Paper).

    Returns:
        str: The result of the game ('Player wins!', 'Computer wins!', 'It's a tie!').
    """
    if player_hand == computer_hand:
        return "It's a tie!"
    elif (player_hand == 0 and computer_hand == 2) or \
         (player_hand == 1 and computer_hand == 0) or \
         (player_hand == 2 and computer_hand == 1):
        return "Player wins!"
    else:
        return "Computer wins!"

# Main part of the game with input validation using while loop
while True:
    try:
        player_input = int(input("Enter a number (0 = Scissors, 1 = Rock, 2 = Paper): "))
        if player_input in [0, 1, 2]:
            break  # Break the loop if the input is valid
        else:
            print("Invalid input! Please enter 0, 1, or 2.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Generate a random hand for the computer
computer_input = random.randint(0, 2)

# Get the string representation of the hands
player_hand = get_hand(player_input)
computer_hand = get_hand(computer_input)

# Print the hands
print(f"Player's hand: {player_hand}")
print(f"Computer's hand: {computer_hand}")

# Determine and print the winner
result = determine_winner(player_input, computer_input)
print(result)