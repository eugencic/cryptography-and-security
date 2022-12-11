# Caesar Cipher

import string


class Caesar:
    # Function to encrypt the message
    def encrypt(self, message, key):
        # Take the shift and do the modulo of the alphabet size
        key %= 26
        # Alphabet
        alphabet = string.ascii_uppercase
        # Shifted alphabet
        # Start at the position where we shift, taking the rest of the list, and append everything before shift 
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        # Translation table where each character in the alphabet will be mapped to the character of the same position
        # in the shifted alphabet
        table = str.maketrans(alphabet, shifted_alphabet)
        # Replace each character in the string using the given translation table
        encrypted_message = message.translate(table)
        return encrypted_message

    # Function to decrypt the message
    def decrypt(self, message, key):
        # Take back the shift and do the modulo of the alphabet size
        key = 26 - key
        key %= 26
        # Alphabet variable
        alphabet = string.ascii_uppercase
        # Shifted alphabet
        # Start at the position where we shift, taking the rest of the list, and append everything before shift 
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        # Translation table where each character in the alphabet will be mapped to the character of the same position
        # in the shifted alphabet
        table = str.maketrans(alphabet, shifted_alphabet)
        # Replace each character in the string using the given translation table
        decrypted_message = message.translate(table)
        return decrypted_message


if __name__ == "__main__":
    caesarCipher = Caesar()
    # Convert to uppercase to coincide with the alphabet
    message = input('Enter the text you want to encrypt: ').upper()
    key = int(input('Enter the key (how much you want to shift): '))
    # Print the original message
    print(f'The original message: {message}')
    # Encrypted message
    encrypted_message = caesarCipher.encrypt(message, key)
    # Print the encrypted message
    print(f'The encrypted message: {encrypted_message}')
    # Decrypted message
    decrypted_message = caesarCipher.decrypt(encrypted_message, key)
    # Print the decrypted message
    print(f'The decrypted message: {decrypted_message}')
