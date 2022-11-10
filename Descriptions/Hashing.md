# SHA-2 Hashing Algorithm

## Theory
&ensp;&ensp;&ensp;The Secure Hash Algorithm 2 (SHA-2) is a computer security cryptographic algorithm. It was created by the US National Security Agency (NSA) in collaboration with the National Institute of Science and Technology (NIST) as an enhancement to the SHA-1 algorithm.

## Steps
* Step 1 - Pre-Processing
* Step 2 – Initialize Hash Values
* Step 3 – Initialize Round Constants
* Step 4 – Chunk Loop
* Step 5 – Create Message Schedule
* Step 6 - Compression
* Step 7 - Modify Final Values

### Pre-Processing
* Convert message to binary
```
binary_message = text2bin(message)
```
* Append a single 1
```
p = binary_message + '1'
```
* Pad with 0’s until data is a multiple of 512, less 64 bits (448 bits in our case)
```
while len(p)%512 != 448:
        p += '0'
```
* Append 64 bits to the end, where the 64 bits are a big-endian integer representing the length of the original input in binary. In our case, 88, or in binary, “1011000”
```
p += bin(message_length)[2:].zfill(64)
```

### Initialize Hash Values
Now we create 8 hash values. These are hard-coded constants that represent the first 32 bits of the fractional parts of the square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19
```
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
```

### Initialize Round Constants
Similar to step 2, we are creating some constants. This time, there are 64 of them. Each value (0-63) is the first 32 bits of the fractional parts of the cube roots of the first 64 primes (2 – 311)
```
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
       0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
       0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
       0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
       0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
       0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
       0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
       0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
```

### Chunk Loop
The following steps will happen for each 512-bit “chunk” of data from our input.

### Create Message Schedule
* Copy the input data from step 1 into a new array where each entry is a 32-bit word
* Modify the zero-ed indexes at the end of the array using the following algorithm:
* For i from w[16…63]:
  * s0 = (w[i-15] rightrotate 7) xor (w[i-15] rightrotate 18) xor (w[i-15] rightshift 3)
  * s1 = (w[i- 2] rightrotate 17) xor (w[i- 2] rightrotate 19) xor (w[i- 2] rightshift 10)
  * w[i] = w[i-16] + s0 + w[i-7] + s1
```
    for l in range(16,64):
        S0 = sigma_0(keys[l-15])
        S1 = sigma_1(keys[l-2])
        w = (keys[l-16] + S0) % pow(2,32) 
        w = (w + keys[l-7]) % pow(2,32) 
        w = (w + S1) % pow(2,32) 
        keys.append(w)
```

### Compression
* Initialize variables a, b, c, d, e, f, g, h and set them equal to the current hash values respectively. h0, h1, h2, h3, h4, h5, h6, h7
* Run the compression loop. The compression loop will mutate the values of a…h. The compression loop is as follows:
* for i from 0 to 63
  * S1 = (e rightrotate 6) xor (e rightrotate 11) xor (e rightrotate 25)
  * ch = (e and f) xor ((not e) and g)
  * temp1 = h + S1 + ch + k[i] + w[i]
  * S0 = (a rightrotate 2) xor (a rightrotate 13) xor (a rightrotate 22)
  * maj = (a and b) xor (a and c) xor (b and c)
  * temp2 := S0 + maj
  * h = g
  * g = f
  * f = e
  * e = d + temp1
  * d = c
  * c = b
  * b = a
  * a = temp1 + temp2
```
    keys = gen_keys(p)
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7
    # Run the main loop 64 times
    for i in range(64):
        e1 = Eta_1(e)
        ch = Chr(e, f, g)
        e0 = Eta_0(a)
        maj = Maj(a, b, c)
        temp1 = (h + e1) % pow(2, 32)
        temp1 = (temp1 + ch) % pow(2, 32)
        temp1 = (temp1 + k[i]) % pow(2, 32)
        temp1 = (temp1 + keys[i]) % pow(2, 32)
        temp2 = (e0 + maj) % pow(2, 32)
        h = g
        g = f
        f = e
        e = (d + temp1) % pow(2, 32)
        d = c
        c = b
        b = a
        a = (temp1 + temp2) % pow(2, 32)
```

### Modify Final Values
After the compression loop, but still, within the chunk loop, we modify the hash values by adding their respective variables to them, a-h. As usual, all addition is modulo 2^32
```
    h0 = bin(h0)[2:].zfill(32)
    h1 = bin(h1)[2:].zfill(32)
    h2 = bin(h2)[2:].zfill(32)
    h3 = bin(h3)[2:].zfill(32)
    h4 = bin(h4)[2:].zfill(32)
    h5 = bin(h5)[2:].zfill(32)
    h6 = bin(h6)[2:].zfill(32)
    h7 = bin(h7)[2:].zfill(32)
```

### Output Example
```
Enter your message: cryptography
0xe06554818e902b4ba339f066967c0000da3fcda4fd7eb4ef89c124fa78bda419
Encrypted message: [191540052, 652807341, 655055403, 191540052, 199010701, 579651635, 579651635, 500503534, 520534102, 374478020, 520534102, 655055403, 590096239, 191540052, 178382036, 452715229, 500503534, 452715229, 9771111, 298708361, 298708361, 590096239, 562955662, 191540052, 199010701, 199010701, 590096239, 199010701, 407865603, 84643015, 191540052, 191540052, 191540052, 191540052, 114959954, 9771111, 298708361, 562955662, 84643015, 114959954, 9771111, 500503534, 562955662, 114959954, 407865603, 655055403, 452715229, 500503534, 655055403, 562955662, 520534102, 590096239, 84643015, 374478020, 178382036, 500503534, 562955662, 9771111, 407865603, 520534102, 452715229, 114959954, 9771111, 500503534, 374478020, 590096239]
Decrypted message: 0xe06554818e902b4ba339f066967c0000da3fcda4fd7eb4ef89c124fa78bda419
Digital signature check is successfull!
```

## Implementation
[Hashing Algorithm](https://github.com/eugencic/utm-cs-labs/blob/main/Code/Hashing.py)