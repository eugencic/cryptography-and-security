# Playfair Cipher

class Playfair:
    # Create a 5x5 matrix using the secret key
    def create_matrix(self, key):
        matrix = [[0 for i in range (5)] for j in range(5)]
        row = 0
        col = 0
        letters_added = []
        # Add the key to the matrix
        for letter in key:
            if letter not in letters_added:
                matrix[row][col] = letter
                letters_added.append(letter)
            else:
                continue
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
        # Add the rest of the alphabet to the matrix
        # A=65 ... Z=90
        for letter in range(65, 91):
            # I/J are in the same position
            if letter == 74:
                continue
            # Do not add repeated letters
            if chr(letter) not in letters_added:
                letters_added.append(chr(letter))      
        index = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = letters_added[index]
                index += 1
        return matrix

    # Add fillers if the same letter is in a pair
    def separate_same_letters(self, message):
        index = 0
        while (index < len(message)):
            l1 = message[index]
            if index == len(message) - 1:
                message = message + 'X'
                index += 2
                continue
            l2 = message[index + 1]
            if l1 == l2:
                message = message[:index + 1] + "X" + message[index + 1:]
            index += 2   
        return message

    # Return the index of a letter in the matrix
    # This will be used to know what rule (1-4) to apply
    def indexOf(self, letter, matrix):
        for i in range(5):
            try:
                index = matrix[i].index(letter)
                return (i, index)
            except:
                continue
        
    # Implementation of the playfair cipher
    # If encrypt = True, the method will encrypt the message. Otherwise, the method will decrypt it
    def playfair(self, message, key, encrypt = True):
        inc = 1
        if encrypt == False:
            inc = -1
        matrix = self.create_matrix(key)
        message = self.separate_same_letters(message)
        cipher_text = ''
        for (l1, l2) in zip(message[0::2], message[1::2]):
            row1, col1 = self.indexOf(l1, matrix)
            row2, col2 = self.indexOf(l2, matrix)
            # Rule 2, the letters are in the same row
            if row1 == row2:
                cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
            # Rule 3, the letters are in the same column    
            elif col1 == col2:
                cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
            # Rule 4, the letters are in a different row and column
            else:
                cipher_text += matrix[row1][col2] + matrix[row2][col1]
        return cipher_text

if __name__=='__main__':
    playfairCipher = Playfair()
    message = (input('Enter the text you want to encrypt: ').upper()).replace(" ", "")
    key = (input('Enter the secret message: ').upper()).replace(" ", "")
    encrypted_message = playfairCipher.playfair(message, key)
    print("Encrypted message: ", encrypted_message) 
    decrypted_message = playfairCipher.playfair(encrypted_message, key, False)
    print("Decrypted message: ", decrypted_message) 