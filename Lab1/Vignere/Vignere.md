# Vignere Cipher

## Theory
&ensp;&ensp;&ensp;Vigenere Cipher is a technique for encrypting alphabetic content. It utilizes a basic type of polyalphabetic replacement. A polyalphabetic cipher is any cipher dependent on replacement, utilizing numerous replacement alphabets.

&ensp;&ensp;&ensp;The table comprises of the letters in order worked out multiple times in various lines, every letter set moved consistently to one side contrasted with the past letters in order, comparing to the 26 potential Caesar Ciphers.

### Initial Step 
&ensp;&ensp;&ensp;Firstly, a key is generated with the help of a keyword if the length of the message is not equal to the keyword.
```
def generateKey(message, key): 
  key = list(key) 
  if len(message) == len(key): 
    return(key) 
  else:
    for i in range(len(message) - len(key)): 
      key.append(key[i % len(key)]) 
  return("".join(key)) 
```
### Encryption
&ensp;&ensp;&ensp;Encrypt the message which takes two arguments. One is the message that needs to be encrypted and the second argument is the key that returns the encrypted text.
```
def encrypt(message, key): 
  alphabet = string.ascii_uppercase
  encrypted_string = ""
  key_position = 0
  for letter in message:
    if letter in alphabet:
      position = alphabet.find(letter)
      key_character = key[key_position]
      key_character_position = alphabet.find(key_character)
      key_position = key_position + 1
      new_position = position + key_character_position
      if new_position > 26:
        new_position = new_position - 26
      new_character = alphabet[new_position]
      encrypted_string = encrypted_string + new_character
    else:
      encrypted_string = encrypted_string + letter
  return(encrypted_string)
```

### Decryption
&ensp;&ensp;&ensp;Same method as encryption, but we take the shift back
```
def decrypt(encrypted_message, key): 
  alphabet = string.ascii_uppercase
  key_position = 0
  decrypted_string = ""
  for letter in encrypted_message:
    if letter in alphabet:
      position = alphabet.find(letter)
      key_character = key[key_position]
      key_character_position = alphabet.find(key_character)
      key_position = key_position + 1
      new_position = position - key_character_position
      if new_position > 26:
        new_position = new_position + 26
      new_character = alphabet[new_position]
      decrypted_string = decrypted_string + new_character
    else:
      decrypted_string = decrypted_string + letter
  return(decrypted_string)
```

### Output Example
```
Enter the text you want to encrypt (uppercase): MEINYOU
Enter the secret message: LOVE
Encrypted message:  XSDRJCP
Decrypted message:  MEINYOU
```
