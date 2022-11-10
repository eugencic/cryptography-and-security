from Code.Caesar import *
from Code.CaesarPermutation import *
from Code.Vignere import *
from Code.Playfair import *
from Code.Stream import *
from Code.Block import *
from Code.Asymmetric import *
from Code.Hashing import *

if __name__ == '__main__':
    print("Caesar Cipher")
    caesarCipher = Caesar()
    message = input('Enter the text you want to encrypt: ').upper()
    key = int(input('Enter the key (how much you want to shift): '))
    print(f'The original message: {message}')
    encrypted_message = caesarCipher.encrypt(message, key)
    print(f'The encrypted message: {encrypted_message}')
    decrypted_message = caesarCipher.decrypt(encrypted_message, key)
    print(f'The decrypted message: {decrypted_message}')
    
    print("Caesar Permutation Cipher")
    caesarPermutationCipher = CaesarPermutation()
    message = input('Enter the text you want to encrypt: ').upper()
    key = (input('Enter the secret message: ').upper()).replace(" ", "")
    shift = int(input('Enter the shift: '))
    print(f'The original message: {message}')
    new_alphabet = caesarPermutationCipher.alphabet_permutation(key)
    print(f'The new alphabet: {new_alphabet}')
    encrypted_message = caesarPermutationCipher.encrypt(message, new_alphabet, shift)
    print(f'The encrypted message: {encrypted_message}')
    decrypted_message = caesarPermutationCipher.decrypt(encrypted_message, new_alphabet, shift)
    print(f'The decrypted message: {decrypted_message}')
    
    print("Vignere Cipher")
    vignereCipher = Vignere() 
    message = input('Enter the text you want to encrypt: ').upper()
    keyword = (input('Enter the secret message: ').upper()).replace(" ", "")
    key = vignereCipher.generateKey(message, keyword) 
    encrypted_message = vignereCipher.encrypt(message, key) 
    print("Encrypted message: ", encrypted_message) 
    decrypted_message = vignereCipher.decrypt(encrypted_message, key) 
    print("Decrypted message: ", decrypted_message)
    
    print("Playfair Cipher")
    playfairCipher = Playfair()
    message = (input('Enter the text you want to encrypt: ').upper()).replace(" ", "")
    key = (input('Enter the secret message: ').upper()).replace(" ", "")
    encrypted_message = playfairCipher.playfair(message, key)
    print("Encrypted message: ", encrypted_message) 
    decrypted_message = playfairCipher.playfair(encrypted_message, key, False)
    print("Decrypted message: ", decrypted_message)
    
    print("RC4 Stream Cipher")
    streamCipher = Stream()
    message = (input('Enter the text you want to encrypt: ').upper()).replace(" ", "")
    key = (input('Enter the secret message: ').upper()).replace(" ", "")
    encrypted_message = streamCipher.encrypt(message, key)
    print("Encrypted message: ", encrypted_message) 
    decrypted_message = streamCipher.decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)
    
    print("Blowfish Block Cipher")
    blockCipher = Block()
    blockCipher.runBlowfish()
    
    print("RSA Asymmetric Cipher")
    asymmetricCipher = Asymmetric()
    private_key, public_key = asymmetricCipher.generate_rsa_keys()
    message = str(input('Enter your message: '))
    cipher = asymmetricCipher.encrypt(public_key, message)
    print('Encrypted message: ' + str(cipher))
    plain = asymmetricCipher.decrypt(private_key, cipher)
    print('Decrypted message: ' + plain)
    
    print("SHA-2 Hashing Algorithm")
    hashing = Hashing()
    message = str(input('Enter your message: '))
    result = hashing.SHA_256(message)
    print(result)
    asymmetricCipher = Asymmetric()
    private_key, public_key = asymmetricCipher.generate_rsa_keys()
    cipher = asymmetricCipher.encrypt(public_key, result)
    print('Encrypted message: ' + str(cipher))
    plain = asymmetricCipher.decrypt(private_key, cipher)
    print('Decrypted message: ' + plain)
    if (plain == result):
        print("Digital signature check is successfull!")
    else:
        print("Error!")