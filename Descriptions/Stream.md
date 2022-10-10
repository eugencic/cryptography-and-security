# RC4 Stream Cipher

## Theory
&ensp;&ensp;&ensp;RC4 stands for Rivest Cipher 4. Ron Rivest invented RC4 in 1987, and it is a stream cipher. Because RC4 is a stream cipher, it encrypts data bytes by bits. Because of its speed and simplicity, RC4 is the most extensively used stream cipher of all the stream ciphers.

RC4 creates a pseudo-random bit stream (a keystream). These, like any other stream cipher, can be used for encryption by utilizing bit-wise exclusive or to combine it with the plaintext. The same procedure is used for decryption (since exclusive-OR is a symmetric operation).


### Key Scheduling Algorithm
&ensp;&ensp;&ensp;The key scheduling algorithm is known to initialize the permutation using a variable-length key, typically between 40 and 256 bits (KSA).
```
def keyScheduling(key):
    # The state vector is from 0 to 255
    S = [i for i in range(0, 256)]
    j = 0
    # Initialize the permutation of S
    for i in range(0, 256):
        # Key scheduling algorithm
        j = (j + S[i] + key[i % len(key)]) % 256
        # Permutation of S
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp
    return S
               
```


### Pseudo Random Generating Algorithm
&ensp;&ensp;&ensp;The key scheduling algorithm is known to initialize the permutation using a variable-length key, typically between 40 and 256 bits (KSA).
```
def streamGeneration(S, text):
    # Generate key stream from the state vector after one more round of permutation
    generated_stream = []
    i, j = 0, 0
    for _ in range(len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # Permutation of S
        S[i], S[j] = S[j], S[i]
        added = (S[i] + S[j]) % 256
        stream = S[added]
        generated_stream.append(stream) 
    return generated_stream
```


### Encryption
* The user enters the Plaintext and a secret key.

* For the secret key entered, the encryption engine creates the keystream using the KSA and PRGA algorithms.

* Plaintext is XORed with the generated keystream. Because RC4 is a stream cipher, byte-by-byte XORing is used to generate the encrypted text.

* This encrypted text is now sent in encrypted form to the intended recipient.
```
def encrypt(text, key):
    # Return the list of characters of the text and the key
    text = [ord(chr) for chr in text]
    key = [ord(chr) for chr in key]
    # Use the key scheduling algorithm
    sched = keyScheduling(key)
    # Use the pseudo random generation algorithm 
    key_stream = streamGeneration(sched, text)
    # Perform XOR between the keystream and the plain text for encryption
    # Convert into binary format
    ciphertext = ''.join(['{:08b}'.format(i ^ j) for i, j in zip(text, key_stream)])
    return ciphertext
```


### Decryption
&ensp;&ensp;&ensp;The same byte-wise X-OR technique is used on the ciphertext to decrypt it.
```
def decrypt(ciphertext, key):
    # Change the encrypted text back to int
    encrypted_text = [int(ciphertext[i:i + 8], 2) for i in range(0, len(ciphertext), 8)]
    # Return the list of characters of the key
    key = [ord(char) for char in key]
    # Use the key scheduling algorithm
    sched = keyScheduling(key)
    # Use the pseudo random generation algorithm 
    key_stream = streamGeneration(sched, ciphertext)
    # Perform XOR between the keystream and the encrypted text for decryption
    # Convert into int format
    plaintext = ''.join(chr(i ^ j) for i, j in zip(encrypted_text, key_stream))
    return plaintext
```


### Output Example
```
Enter E for Encrypt, or D for Decrypt: E
Enter your text: EUGENIU1234
Enter your secret key: secret
Result: 1010100001100011100101010101100111001100111011011000001110010111000000001111100010001111

Enter E for Encrypt, or D for Decrypt: D
Enter your encrypted text: 1010100001100011100101010101100111001100111011011000001110010111000000001111100010001111
Enter your secret key: secret
Result: EUGENIU1234
```


## Implementation
[Stream Cipher](https://github.com/eugencic/utm-cs-labs/blob/main/Code/Stream.py)