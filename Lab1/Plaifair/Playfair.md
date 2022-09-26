# Playfair Cipher

## Theory
&ensp;&ensp;&ensp;The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet. It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment.

### Steps
&ensp;&ensp;&ensp;The steps to implement the cipher are as follows:
* Create a 5×5 matrix using the secrete key. In this matrix, I and J are in the same cell. you start filling the matrix with the key, then you use the alphabet. Letters are placed only once in the matrix.
* We encrypt the message using two letters each time. To do that, we follow four rules:
  - When you get two letters, if they are the same letter, you add a “filler” in the middle. It can be the letter ‘x’.
  - If the two letters fall in the same row of the matrix, you substitute them with the next letter in the row. Rows have a circular behavior. The next letter of the last in a row is the first letter in that row.
  - If the two letters fall in the same column of the matrix, you substitute them with the next letter in the column (going down). Columns have a circular behavior. The next letter of the last in a column is the first letter in that column.
  - If the two letters are not in the same row and column, then you substitute each letter by the letter in the same row and the column of the second letter.

### Matrix
&ensp;&ensp;&ensp;Create a 5x5 matrix using a secret key.
```
def create_matrix(key):
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
        if (col == 4):
            col = 0
            row += 1
        else:
            col += 1
    #Add the rest of the alphabet to the matrix
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
```

### Filters
&ensp;&ensp;&ensp;Add fillers if the same letter is in a pair.
```
def separate_same_letters(message):
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
```

### Encryption and Decryption
&ensp;&ensp;&ensp;If encrypt = True, the method will encrypt the message. Otherwise the method will decrypt it.
```
def playfair(message, key, encrypt = True):
    inc = 1
    if encrypt == False:
        inc = -1
    matrix = create_matrix(key)
    message = separate_same_letters(message)
    cipher_text = ''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        # Rule 2, the letters are in the same row
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        # Rule 3, the letters are in the same column    
        elif col1 == col2:
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        #Rule 4, the letters are in a different row and column
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text

```

### Output Example
```
Enter the text you want to encrypt (uppercase): IlovEyou
Enter the secret message: secret
Encrypted message:  KMNWRWPN
Decrypted message:  ILOVEYOU
```
