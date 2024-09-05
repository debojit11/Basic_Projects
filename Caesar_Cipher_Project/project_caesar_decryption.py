lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
encrypted_message = "P olhy aol nvvzlilyyplz hyl kvpun dlss aopz flhy, huk zv hyl aol thunvlz."
cipher = 7
decrypted_message = ""
for char in encrypted_message:
    if char.islower():
        index = lowercase_letters.index(char)
        new_index = (index - cipher) % 26
        decrypted_message += lowercase_letters[new_index]
    elif char.isupper():
        index = lowercase_letters.index(char.lower())
        new_index = (index - cipher) % 26
        decrypted_message += lowercase_letters[new_index].upper()
    else:
        decrypted_message += char
           

print(decrypted_message) 