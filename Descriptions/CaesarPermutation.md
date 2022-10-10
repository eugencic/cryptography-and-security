# Caesar Cipher

## Theory
&ensp;&ensp;&ensp;It is a type of mono-alphabetic permutation cipher where the letters of the alphabet are arranged based on a given key.

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


## Implementation
[Caesar Permutation Cipher](https://github.com/eugencic/utm-cs-labs/blob/main/Code/CaesarPermutation.py)