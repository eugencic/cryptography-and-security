# RSA Asymmetric Cipher

## Theory
&ensp;&ensp;&ensp;RSA encryption algorithm is a type of public-key encryption algorithm.

Public Key encryption algorithm is also called the Asymmetric algorithm. Asymmetric algorithms are those algorithms in which sender and receiver use different keys for encryption and decryption. Each sender is assigned a pair of keys:
- Public key
- Private key

The Public key is used for encryption, and the Private Key is used for decryption. Decryption cannot be done using a public key. The two keys are linked, but the private key cannot be derived from the public key. The public key is well known, but the private key is secret and it is known only to the user who owns the key. It means that everybody can send a message to the user using user's public key. But only the user can decrypt the message using his private key.


### Algorithm Implementation
1. First, the receiver chooses two large prime numbers p and q. Their product, n = pq, will be half of the public key.
```
    # Generate the first huge random prime numbers
    p = generate_large_prime()
    q = generate_large_prime()           
```
```
    # Function to generate a large prime number
    def generate_large_prime(start = RANDOM_START, end = RANDOM_END):
    # Generate a random number [RANDOM_START, RANDOM_END]
    num = random.randint(start, end)
    # And check wether it is prime or not
    while not is_prime(num):
        num = random.randint(start, end)
    # We know the number is prime
    return num           
```

2. The receiver calculates ϕ(pq) = (p-1)(q-1) and chooses a number e relatively prime to ϕ(pq).
```
    # Generate the first huge random prime numbers
    p = generate_large_prime()
    q = generate_large_prime()
    # This is the trapdoor funciton. Multiplying is fast but getting p and q from n is an expoentially slow operation
    n = p * q
    # Euler's tottient phi function
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    # We must make sure gcd(e, phi) = 1, so e and phi are coprimes, otherwise we cannot find d
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)        
```

3. The receiver calculates the modular inverse d of e modulo ϕ(n).
```
    # Extended Euclid's algorithm to find modular inverse in O(log m) in linear time
    # This is how we can find the d value which is the modular inverse of e in the RSA cryptosystem
    def modular_inverse(a, b):
        if a == 0:
            return b, 0, 1
        # So we use the Euclidean algorithm for gcd()
        # b % a is always the smaller number - and 'a' is the smaller integer in this implementation
        div, x1, y1 = modular_inverse(b % a, a)
        # And we update the parameters for x, y accordingly
        x = y1 - (b // a) * x1
        y = x1
        # We use recursion so this is how we send the result to the previous stack frame
        return div, x, y        
```

4. The receiver distributes both parts of the public key: n and e. d is kept secret.


### Encryption
Consider a sender who sends the plain text message to someone whose public key is (n,e). To encrypt the plain text message in the given scenario, use the following syntax - `C = Pe mod n`
```
def encrypt(public_key, plain_text):
    # e and n are needed for encryption
    e, n = public_key
    # We use ASCII  representation for the characters and the transformation of every character is stored in an array
    cipher_text = []
    # Consider all the letters one by one and use modular exponentiation
    for char in plain_text:
        a = ord(char)
        cipher_text.append(pow(a, e, n))
    return cipher_text
```


### Decryption
&ensp;&ensp;&ensp;The decryption process is very straightforward and includes analytics for calculation in a systematic approach. Considering receiver C has the private key d, the result modulus will be calculated as − `Plaintext = Cd mod n`
```
def decrypt(private_key, cipher_text):
    # d and n are needed for decryption
    d, n = private_key
    plain_text = ''
    for num in cipher_text:
        a = pow(num, d, n)
        plain_text = plain_text + str(chr(a))
    return plain_text
```


### Output Example
```
Enter your message: technical university of moldova
Encrypted message: [644882587, 53035934, 363298011, 257812826, 154045049, 138031260, 363298011, 167004075, 239027131, 153785534, 869301333, 154045049, 138031260, 545539606, 53035934, 91658304, 919835015, 138031260, 644882587, 344265791, 153785534, 504800687, 87403692, 153785534, 221601064, 504800687, 239027131, 888057474, 504800687, 545539606, 167004075]
Decrypted message: technical university of moldova
```


## Implementation
[Asymmetric Cipher](https://github.com/eugencic/utm-cs-labs/blob/main/Code/Asymmetric.py)