# Playfair Cipher

## Theory
&ensp;&ensp;&ensp;The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet.
&ensp;&ensp;&ensp;It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment.

### Steps
&ensp;&ensp;&ensp;The steps to implement the cipher are as follows:
* Create a 5×5 matrix using the secrete key. In this matrix, I and J are in the same cell. you start filling the matrix with the key, then you use the alphabet. Letters are placed only once in the matrix.
* We encrypt the message using two letters each time. To do that, we follow four rules:
  - When you get two letters, if they are the same letter, you add a “filler” in the middle. It can be the letter ‘x’.
  - If the two letters fall in the same row of the matrix, you substitute them with the next letter in the row. Rows have a circular behavior. The next letter of the last in a row is the first letter in that row.
  - If the two letters fall in the same column of the matrix, you substitute them with the next letter in the column (going down). Columns have a circular behavior. The next letter of the last in a column is the first letter in that column.
  - If the two letters are not in the same row and column, then you substitute each letter by the letter in the same row and the column of the second letter.

### Initial Step 
&ensp;&ensp;&ensp;Create a new alphabet, by adding the unique characters from the message and then all the remaining alphabet letters
```
def alphabet_permutation(secret):
    # Alphabet
    alphabet = string.ascii_uppercase
    # Add the unique characters from the key
    new_alphabet = "".join(sorted(set(secret), key = secret.index))
    # Add the remaining letters from the alphabet
    for letter in alphabet:
        if letter not in new_alphabet:
            new_alphabet += letter
```

### Aplhabet Shift
&ensp;&ensp;&ensp;Create the shifted alphabet
```
# Shifted alphabet
# Start at the position where we shift, taking the rest of the list, and append everything before shift 
shifted_alphabet = alphabet[key:] + alphabet[:key]
```

### Encryption
&ensp;&ensp;&ensp;Each character in the alphabet will be mapped to the character of the same position in the shifted alphabet 
```
# Translation table where each character in the alphabet will be mapped to the character of the same position in the shifted alphabet 
table = str.maketrans(alphabet, shifted_alphabet)
# Replace each character in the string using the given translation table
encrypted_message = message.translate(table)
```

### Decryption
&ensp;&ensp;&ensp;Same method as encryption, but we take the shift back
```
# Take back the shift and do the modulo of the alphabet size
key = 26 - key
key %= 26
```

### Output Example
```
Enter the text you want to encrypt (uppercase): MEINYOU
Enter the secret message: LOVE
Enter the shift: 5
The original message: MEINYOU
The new alphabet: LOVEABCDFGHIJKMNPQRSTUWXYZ
The encrypted message: SFPTECL
The decrypted message: MEINYOU
```
