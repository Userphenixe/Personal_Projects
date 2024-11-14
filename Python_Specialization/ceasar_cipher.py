alphabet = 'abcdefghijklmnopqrstuvwxyz'

def out_index(i):
    return i % 26

def caesar_cipher(stri, shift):
    if type(stri) != str:
        print('Please enter a string')
        return None
    elif len(stri) <= 0:
        print('Please enter a sequence of characters')
        return None
    else:
        output = ''
        for char in stri:
            if char not in alphabet:
                output += char  # Non-alphabet characters are added unchanged
            else:
                index = alphabet.index(char)  # Get the current position in the alphabet
                new_index = out_index(index + shift)  # Apply the shift with wrap-around
                output += alphabet[new_index]  # Append shifted character to output
        return output

# Testing encryption and decryption
encrypted = caesar_cipher('bhjbbmaa,l>zxxbshhJB,.KN.K.dk', 3)
print("Encrypted:", encrypted)  # Encrypted output
decrypted = caesar_cipher(encrypted, -3)
print("Decrypted:", decrypted)  # Decrypted output
