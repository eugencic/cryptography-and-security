# RSA Asymmetric Cipher

import random 
from math import floor
from math import sqrt

# Generate random numbers from 1000 to 100000
RANDOM_START = 1e3
RANDOM_END = 1e5

# Class of the Asymmetric Cipher
class Asymmetric:
    # Function to check and return if the number is prime
    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, floor(sqrt(num))):
            if num % i == 0:
                return False
        return True

    # Euclid's greatest common divisor algorithm. This is how we can verify wether (e, φ) = 1 are coprime with the gcd(e, φ) = 1 condition
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Extended Euclid's algorithm to find modular inverse in O(log m) in linear time
    # This is how we can find the d value which is the modular inverse of e in the RSA cryptosystem
    def modular_inverse(self, a, b):
        if a == 0:
            return b, 0, 1
        # So we use the Euclidean algorithm for gcd()
        # b % a is always the smaller number - and 'a' is the smaller integer in this implementation
        div, x1, y1 = self.modular_inverse(b % a, a)
        # And we update the parameters for x, y accordingly
        x = y1 - (b // a) * x1
        y = x1
        # We use recursion so this is how we send the result to the previous stack frame
        return div, x, y

    # Function to generate a large prime number
    def generate_large_prime(self, start = RANDOM_START, end = RANDOM_END):
        # Generate a random number [RANDOM_START, RANDOM_END]
        num = random.randint(start, end)
        # And check wether it is prime or not
        while not self.is_prime(num):
            num = random.randint(start, end)
        # We know the number is prime
        return num

    def generate_rsa_keys(self):
        # Generate the first huge random prime numbers
        p = self.generate_large_prime()
        q = self.generate_large_prime()
        # This is the trapdoor funciton. Multiplying is fast but getting p and q from n is an expoentially slow operation
        n = p * q
        # Euler's tottient phi function
        phi = (p-1) * (q-1)
        e = random.randrange(1, phi)
         # We must make sure gcd(e, phi) = 1, so e and phi are coprimes, otherwise we cannot find d
        while self.gcd(e, phi) != 1:
            e = random.randrange(1, phi)
        # d is the modular inverse of e
        # We put [1], because we want to get the index 1 which is the value of x
        d = self.modular_inverse(e, phi)[1]
        # Private key and the public key
        return (d, n), (e, n)

    def encrypt(self, public_key, plain_text):
        # e and n are needed for encryption
        e, n = public_key
        # We use ASCII  representation for the characters and the transformation of every character is stored in an array
        cipher_text = []
        # Consider all the letters one by one and use modular exponentiation
        for char in plain_text:
            a = ord(char)
            cipher_text.append(pow(a, e, n))
        return cipher_text

    def decrypt(self, private_key, cipher_text):
        # d and n are needed for decryption
        d, n = private_key
        plain_text = ''
        for num in cipher_text:
            a = pow(num, d, n)
            plain_text = plain_text + str(chr(a))
        return plain_text

if __name__ == '__main__':
    asymmetricCipher = Asymmetric()
    private_key, public_key = asymmetricCipher.generate_rsa_keys()
    message = str(input('Enter your message: '))
    cipher = asymmetricCipher.encrypt(public_key, message)
    print('Encrypted message: ' + str(cipher))
    plain = asymmetricCipher.decrypt(private_key, cipher)
    print('Decrypted message: ' + plain)