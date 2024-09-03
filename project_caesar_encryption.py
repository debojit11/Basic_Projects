lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
encrypted_message = ""
for char in secret:
    if char.islower():
        index = lowercase_letters.index(char)
        new_index = (index + cipher) % 26
        encrypted_message += lowercase_letters[new_index]
    elif char.isupper():
        index = lowercase_letters.index(char.lower())
        new_index = (index + cipher) % 26
        encrypted_message += lowercase_letters[new_index].upper()
    else:
        encrypted_message += char
           

print(encrypted_message) 