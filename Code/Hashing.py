# SHA-2 Hashing Algorithm

from Asymmetric import *

class Hashing:
    # Text to binary
    def text2bin(self, message):
        output = ''
        for i in message:
            output += bin(ord(i))[2:].zfill(8)
        return output

    # Bitwise rotation of a number rotdist bits to the right, inside the field defined by bit_length
    def ROR(self, number, rotdist, bit_length):
        a = number.zfill(bit_length)
        # Loop over the number of rotations needed
        for i in range(rotdist):
            # Perform one rotation at a time
            b = ''
            # Do the loop first
            b = b + a[bit_length - 1]
            # Move all the other elements in the string
            for l in range(bit_length - 1):
                b = b + a[l]
            # Alter a to ensure perminance over all the shifts in the code a = int(b, 2)
            a = b
        return a

    # SHA-2 specific functions

    # Padding the message out
    def padding_function(self, message):
        # Convert the message to a string
        binary_message = self.text2bin(message)
        # Record the initial message length for later
        message_length = len(binary_message)
        # Add one to the end of the message string
        p = binary_message + '1'
        # Extend the length of p until len(p) % 512 = 448
        while len(p)%512 != 448:
            p += '0'
        # The final padding step, add the length of the starting message
        p += bin(message_length)[2:].zfill(64)
        block_no = int(len(p)/512)
        # Split the padded message in blocks
        blocks = []
        for i in range(block_no):
            blocks.append(p[i * 512: (i * 512) + 512])
        return blocks

    # Functions that are used by the loop

    # XOR
    # AND
    # NOT
    # ROR(x, n) = rotate x right by n
    # x >> n = right shift x by n

    # s0 = ROR(x,7) ^ ROR(x,18) ^ x >> 3
    def sigma_0(self, x):
        sigma0 = int(self.ROR(bin(x)[2:], 7, 32), 2) ^ int(self.ROR(bin(x)[2:], 18, 32), 2) ^ (x >> 3)
        return sigma0

    # s1 = ROR(x,17) ^ ROR(x,19) ^ x >> 10
    def sigma_1(self, x):
        sigma1 = int(self.ROR(bin(x)[2:], 17, 32), 2) ^ int(self.ROR(bin(x)[2:], 19, 32), 2) ^ (x >> 10)
        return sigma1

    # e0 = ROR(x,2) ^ ROR(x,13) ^ ROR(x,22)
    def Eta_0(self, x):
        Eta_0 = int(self.ROR(bin(x)[2:], 2, 32), 2) ^ int(self.ROR(bin(x)[2:], 13, 32), 2) ^ int(self.ROR(bin(x)[2:], 22, 32), 2)
        return Eta_0

    # e1 = ROR(x,6) ^ ROR(x,11) ^ ROR(x,25)
    def Eta_1(self, x):
        Eta_1 = int(self.ROR(bin(x)[2:], 6, 32), 2) ^ int(self.ROR(bin(x)[2:], 11, 32), 2) ^ int(self.ROR(bin(x)[2:], 25, 32), 2)
        return Eta_1

    # Chr = (x & y) ^ (x & z)
    def Chr(self, x, y, z):
        NOT = 0b11111111111111111111111111111111
        Chr = (x & y) ^ ((x ^ NOT) & z)
        return Chr

    # Maj = (x & y) ^ (x & z) ^ (y & z)
    def Maj(self, x, y, z):
        Maj = (x & y) ^ (x & z) ^ (y & z)
        return Maj

    # Functions that do the major bits of SHA-256
    def gen_keys(self, block):
        keys = []
        for i in range(16):
            keys.append(int(block[(i * 32) : ((i * 32) + 32)], 2))
        # Make 48 new keys using the formula key[i] = key[i-16] ^ s0(key[i-15]) ^ key[i-7] ^ s1(key[i-2])
        for l in range(16,64):
            S0 = self.sigma_0(keys[l-15])
            S1 = self.sigma_1(keys[l-2])
            w = (keys[l-16] + S0) % pow(2,32) 
            w = (w + keys[l-7]) % pow(2,32) 
            w = (w + S1) % pow(2,32) 
            keys.append(w)
        return keys

    def SHA_256(self, message):
        # Initialise the first h values
        h0 = 0x6a09e667
        h1 = 0xbb67ae85
        h2 = 0x3c6ef372
        h3 = 0xa54ff53a
        h4 = 0x510e527f
        h5 = 0x9b05688c
        h6 = 0x1f83d9ab
        h7 = 0x5be0cd19

        # Initialise the round constants
        k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

        # Convert the message into 512 bit blocks by padding it out
        blocks = self.padding_function(message)
        for p in blocks:
            # Generate the keys. This is where the block actually gets processed
            keys = self.gen_keys(p)
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
                e1 = self.Eta_1(e)
                ch = self.Chr(e, f, g)
                e0 = self.Eta_0(a)
                maj = self.Maj(a, b, c)
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
            # Save the results by adding them to the previous results
            h0 = (h0 + a) % pow(2, 32)
            h1 = (h1 + b) % pow(2, 32)
            h2 = (h2 + c) % pow(2, 32)
            h3 = (h3 + d) % pow(2, 32)
            h4 = (h4 + e) % pow(2, 32)
            h5 = (h5 + f) % pow(2, 32)
            h6 = (h6 + g) % pow(2, 32)
            h7 = (h7 + h) % pow(2, 32)

        # Convert the results to 32 bit binary words for the final result
        h0 = bin(h0)[2:].zfill(32)
        h1 = bin(h1)[2:].zfill(32)
        h2 = bin(h2)[2:].zfill(32)
        h3 = bin(h3)[2:].zfill(32)
        h4 = bin(h4)[2:].zfill(32)
        h5 = bin(h5)[2:].zfill(32)
        h6 = bin(h6)[2:].zfill(32)
        h7 = bin(h7)[2:].zfill(32)

        # Add the results using the endian convention
        result = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
        result = hex(int(result, 2))
        return result

if __name__ == "__main__":
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