# Vignere Cipher

import string


class Vignere:
    # Firstly, a key is generated with the help of a keyword if the length of the message is not equal to the keyword
    def generateKey(self, message, key):
        key = list(key)
        if len(message) == len(key):
            return (key)
        else:
            # The keyword is appended to itself until the length of the message is equal to the length of the key
            for i in range(len(message) - len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

        # Encrypt the message which takes two arguments. One is the message that needs to be encrypted and the second
        # argument is the key that returns the encrypted text

    def encrypt(self, message, key):
        # Alphabet
        alphabet = string.ascii_uppercase
        # Key posotion
        # Encrypted string
        encrypted_string = ""
        key_position = 0
        for letter in message:
            if letter in alphabet:
                # Cycle through each letter to find its numeric position in the alphabet
                position = alphabet.find(letter)
                # Move along the key and find the characters value
                key_character = key[key_position]
                key_character_position = alphabet.find(key_character)
                key_position = key_position + 1
                # Change the original message
                new_position = position + key_character_position
                # Go from the beginning if the position number is bigger than the alphabet number
                if new_position > 26:
                    new_position = new_position - 26
                new_character = alphabet[new_position]
                encrypted_string = encrypted_string + new_character
            else:
                encrypted_string = encrypted_string + letter
        return (encrypted_string)

    # Decrypt the message which takes two arguments. One is the message that needs to be encrypted and the second
    # argument is the key that returns the encrypted text
    def decrypt(self, encrypted_message, key):
        # Alphabet
        alphabet = string.ascii_uppercase
        # Key position
        key_position = 0
        # Decrypted string
        decrypted_string = ""
        for letter in encrypted_message:
            if letter in alphabet:
                # Cycle through each letter to find its numeric position in the alphabet
                position = alphabet.find(letter)
                # Move along the key and find the characters value
                key_character = key[key_position]
                key_character_position = alphabet.find(key_character)
                key_position = key_position + 1
                # Change the original message
                new_position = position - key_character_position
                # Go from the beginning if the position number is bigger than the alphabet number
                if new_position > 26:
                    new_position = new_position + 26
                new_character = alphabet[new_position]
                decrypted_string = decrypted_string + new_character
            else:
                decrypted_string = decrypted_string + letter
        return (decrypted_string)


if __name__ == "__main__":
    vignereCipher = Vignere()
    message = input('Enter the text you want to encrypt: ').upper()
    keyword = (input('Enter the secret message: ').upper()).replace(" ", "")
    key = vignereCipher.generateKey(message, keyword)
    encrypted_message = vignereCipher.encrypt(message, key)
    print("Encrypted message: ", encrypted_message)
    decrypted_message = vignereCipher.decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)
