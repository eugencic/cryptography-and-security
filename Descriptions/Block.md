# Blowfish Block Cipher

## Theory
&ensp;&ensp;&ensp;Blowfish is the symmetric block cipher algorithm and it encrypts the block information of 64-bits at a time. It follows the Feistel network and the working procedure of this algorithm is divided into two parts.

* Sub-key Generation − This process transform the key up to 448 bits long to subkeys adding 4168 bits.

* Data-Encryption − In the data encryption process, it will iterate 16 times of network. Each round includes the key-dependent permutation, and the keyand data-dependent substitution. The operations in the algorithms are XORs or additions on 32-bit words. The only additional operations are four indexed array information lookups per round.


### Sub-key Generation
&ensp;&ensp;&ensp;Blowfish cryptographic algorithm uses a huge number of sub keys. These keys are creating earlier to any of the data encryption or the decryption.

The p-array includes 18, 32-bit sub keys −

P1,P2,………….,P18.

There are four 32-bit S-Boxes includes 256 entries each −

S1,0, S1,1,………. S1,255

S2,0, S2,1,……….. S2,255

S3,0, S3,1,……….. S3,255

S4,0, S4,1,………... S4,255

- Steps to generate Sub-keys

    - Initialize first, the P-array and therefore the four S-boxes, in order, with a fixed string and also this string also includes the hexadecimal digits of π.

    - P1=0x243f6a88, P2=0x85a308d3, P3=0x13198a2e, P4=0x3707344, etc.

    - XOR P1 with the first 32 bits of the key, XOR P2 with second which is 32-bits of the key, etc. for all bits of the key (conceivably up to P14). Repeatedly cycles the procedure through the key bits until the complete P-array has been XORed with key bits. (For each short key, there is partly one equivalent longer key. For example, if A is a 64-bit key, then AA, AAA, etc., are same keys.)
    ```
    def subkey_generation(key):
    for i in range(0, 18):
        p[i] = p[i] ^ key[i % len(key)]
    ```

    - It can encrypt the all-zero string with the Blowfish algorithm, utilizing the subkeys defined in step 1 and step 2.

    - It can restore P1 and P2 with the 64 bit output of step (3).

    - It can encrypt the output of step (3) using the algorithm with the changed subkeys.

    - It can restore P3 and P4 with the output of step (5).

    - It can be used to continue the procedure, restoring all entries of P array, and then all four S-boxes in order, with the output of the continuously changing algorithm.

    - In total 521 iterations are needed to make all required subkeys. Application can save the subkeys instead of execute this derivation process, multiple times.


### Encryption
&ensp;&ensp;&ensp;Blowfish is a Feistel network including 16 rounds.

The input is a 64-bit data element, x.

Divide x into two 32-bit halves : xL, xR.

Then, for i = 1 to 16;

xL = xLXOR Pi

xR = F(xL) XOR xR

Swap xL and xR

After the 16th round, Swap xL and xR again to undo the last swap.

Then, ciphertext = concatenation of xL and xR, xR = xR XOR P17 and xL = xL XOR P18.

Finally, recombine xL and xR to get the ciphertext.
```
def encrypt(data):
    xL = data >> 32
    xR = data & 0xffffffff
    for i in range(0, 16):
        xL = xL ^ p[i]
        xR = functionF(xL) ^ xR
        xL, xR = swap(xL, xR)
    xL, xR = swap(xL, xR)
    xR = xR ^ p[16]
    xL = xL ^ p[17]
    encrypted_data = (xL << 32) ^ xR
    return encrypted_data
```


### Decryption
&ensp;&ensp;&ensp;Decryption is the equivalent as encryption, other than P1, P2,……P18 are utilized in the reverse order.
```
def decrypt(data):
    xL = data >> 32
    xR = data & 0xffffffff
    for i in range(17, 1, -1):
        xL = xL ^ p[i]
        xR = functionF(xL) ^ xR
        xL, xR = swap(xL, xR)
    xL, xR = swap(xL, xR)
    xR = xR ^ p[1]
    xL = xL ^ p[0]
    decrypted_data = (xL << 32) ^ xR
    return decrypted_data
```


### Feistel Network
&ensp;&ensp;&ensp;A Feistel network is a cryptographic technique used in the construction of block cipher-based algorithms and mechanisms. 

A Feistel network implements a series of iterative ciphers on a block of data and is generally designed for block ciphers that encrypt large quantities of data. A Feistel network works by splitting the data block into two equal pieces and applying encryption in multiple rounds. Each round implements permutation and combinations derived from the primary function or key. The number of rounds varies for each cipher that implements a Feistel network.

Moreover, as a reversible algorithm, a Feistel network produces the same output until the input is the same.


### Implementation Errors
&ensp;&ensp;&ensp;Some values might generate an IndexError, while other values cannot fit 'int' into an index-sized integer. Small strings will work.


### Output Example
```
Enter your text: eugeniu
Encrypted message: 476081950619411674
Decrypted message: eugeniu
```
