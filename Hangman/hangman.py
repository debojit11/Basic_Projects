# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

word = "problematic"
blanks = ["_"] * len(word)
tries = 0
max_tries = 10
guessed_letters = []  # To track letters already guessed

while tries < max_tries:
    print("Word to guess: ", " ".join(blanks))  # Show current state of word
    guess = input("Enter a letter: ")

    # Check if input is valid
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)  # Track the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess  # Fill the correct guess in the blanks
            print("Good guess! Current word:", " ".join(blanks))  # Showing updated blanks
            if "_" not in blanks:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            tries += 1
            guessed_letters.append(guess)  # Track the incorrect guessed letter too
            print(f"Incorrect guess. Tries remaining: {max_tries - tries}")
    else:
        print("Please enter a single alphabetic character.")
    
    if tries == max_tries:
        print("Sorry, you've run out of tries. The word was:", word)
