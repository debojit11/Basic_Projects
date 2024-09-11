import string

# Take a sentence input from the user
sentence = input("Enter a sentence: ")

# Initialize a dictionary to store the counts
char_count = {
    "Upper case": 0,
    "Lower case": 0,
    "Punctuation": 0,
    "Total chars": 0
}

for char in sentence:
    if char.isupper():
        char_count["Upper case"] += 1
    elif char.islower():
        char_count["Lower case"] += 1
    elif char in string.punctuation:
        char_count["Punctuation"] += 1
    
    # Count total characters except spaces
    if char != ' ':
        char_count["Total chars"] += 1

for key, value in char_count.items():
    print(f"{key}: {value}")
