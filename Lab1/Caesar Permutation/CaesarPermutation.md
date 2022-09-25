# Caesar Cipher

## Theory
&ensp;&ensp;&ensp;In cryptography, a Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

### Initial Step 
&ensp;&ensp;&ensp;Create the shifted alphabet
```
# Alphabet
alphabet = string.ascii_uppercase
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
Enter the key (how much you want to shift): 5
The original message: MEINYOU
The encrypted message: RJNSDTZ
The decrypted message: MEINYOU
```
