# RC4 Stream Cipher

# Key scheduling algorithm
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
    
# Pseudo random generation algorithm (Stream generation)
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


if __name__ == '__main__':
    text = input('Enter E for Encrypt, or D for Decrypt: ').upper()
    if text == 'E':
        plaintext = input('Enter your text: ')
        key = input('Enter your secret key: ')
        result = encrypt(plaintext, key)
        print(f'Result: {result}')
    elif text == 'D': 
        ciphertext = input('Enter your encrypted text: ')
        key = input('Enter your secret key: ')
        result = decrypt(ciphertext, key)
        print(f'Result: {result}')
    else:
        print('Something went wrong. Try again.')