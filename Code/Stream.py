# RC4 Stream Cipher

class Stream:
    # Key scheduling algorithm
    def keyScheduling(self, key):
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
    def streamGeneration(self, S, text):
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
               
    def encrypt(self, text, key):
        # Return the list of characters of the text and the key
        text = [ord(chr) for chr in text]
        key = [ord(chr) for chr in key]
        # Use the key scheduling algorithm
        sched = self.keyScheduling(key)
        # Use the pseudo random generation algorithm 
        key_stream = self.streamGeneration(sched, text)
        # Perform XOR between the keystream and the plain text for encryption
        # Convert into binary format
        ciphertext = ''.join(['{:08b}'.format(i ^ j) for i, j in zip(text, key_stream)])
        return ciphertext

    def decrypt(self, ciphertext, key):
        # Change the encrypted text back to int
        encrypted_text = [int(ciphertext[i:i + 8], 2) for i in range(0, len(ciphertext), 8)]
        # Return the list of characters of the key
        key = [ord(char) for char in key]
        # Use the key scheduling algorithm
        sched = self.keyScheduling(key)
        # Use the pseudo random generation algorithm 
        key_stream = self.streamGeneration(sched, ciphertext)
        # Perform XOR between the keystream and the encrypted text for decryption
        # Convert into int format
        plaintext = ''.join(chr(i ^ j) for i, j in zip(encrypted_text, key_stream))
        return plaintext

if __name__ == '__main__':
    streamCipher = Stream()
    message = (input('Enter the text you want to encrypt: ').upper()).replace(" ", "")
    key = (input('Enter the secret message: ').upper()).replace(" ", "")
    encrypted_message = streamCipher.encrypt(message, key)
    print("Encrypted message: ", encrypted_message) 
    decrypted_message = streamCipher.decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)