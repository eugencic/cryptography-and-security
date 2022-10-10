import string

# Function to create the new permuted alphabet
def alphabet_permutation(secret):
    # Alphabet
    alphabet = string.ascii_uppercase
    # Add the unique characters from the key
    new_alphabet = "".join(sorted(set(secret), key = secret.index))
    # Add the remaining letters from the alphabet
    for letter in alphabet:
        if letter not in new_alphabet:
            new_alphabet += letter
    return new_alphabet

# Function to encrypt the message
def encrypt(message, alphabet, key):
    # Take the shift and do the modulo of the alphabet size
    key %= 26
    # Shifted alphabet
    # Start at the position where we shift, taking the rest of the list, and append everything before shift 
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    # Translation table where each character in the alphabet will be mapped to the character of the same position in the shifted alphabet 
    table = str.maketrans(alphabet, shifted_alphabet)
    # Replace each character in the string using the given translation table
    encrypted_message = message.translate(table)
    return encrypted_message

# Function to decrypt the message
def decrypt(message, alphabet, key):
    # Take back the shift and do the modulo of the alphabet size
    key = 26 - key
    key %= 26
    # Shifted alphabet
    # Start at the position where we shift, taking the rest of the list, and append everything before shift 
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    # Translation table where each character in the alphabet will be mapped to the character of the same position in the shifted alphabet 
    table = str.maketrans(alphabet, shifted_alphabet)
    # Replace each character in the string using the given translation table
    decrypted_message = message.translate(table)
    return decrypted_message

if __name__ == "__main__": 
    # Convert to uppercase to coincide with the alphabet
    message = input('Enter the text you want to encrypt (uppercase): ').upper()
    key = (input('Enter the secret message (uppercase): ').upper()).replace(" ", "")
    shift = int(input('Enter the shift: '))
    # Print the original message
    print(f'The original message: {message}')
    # New alphabet
    new_alphabet = alphabet_permutation(key)
    # Print the new alphabet
    print(f'The new alphabet: {new_alphabet}')
    # Encrypted message
    encrypted_message = encrypt(message, new_alphabet, shift)
    # Print the encrypted message
    print(f'The encrypted message: {encrypted_message}')
    # Decrypted message
    decrypted_message = decrypt(encrypted_message, new_alphabet, shift)
    # Print the decrypted message
    print(f'The decrypted message: {decrypted_message}')