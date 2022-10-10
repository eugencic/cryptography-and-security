# Topic: Symmetric Ciphers. Stream Ciphers. Block Ciphers.

### Course: Cryptography & Security
### Author: Eugeniu Popa

----

## Overview
&ensp;&ensp;&ensp; Symmetric Cryptography deals with the encryption of plain text when having only one encryption key which needs to remain private. Based on the way the plain text is processed/encrypted there are 2 types of ciphers:
- Stream ciphers:
    - The encryption is done one byte at a time.
    - Stream ciphers use confusion to hide the plain text.
    - Make use of substitution techniques to modify the plain text.
    - The implementation is fairly complex.
    - The execution is fast.
- Block ciphers:
    - The encryption is done one block of plain text at a time.
    - Block ciphers use confusion and diffusion to hide the plain text.
    - Make use of transposition techniques to modify the plain text.
    - The implementation is simpler relative to the stream ciphers.
    - The execution is slow compared to the stream ciphers.

&ensp;&ensp;&ensp; Some examples of stream ciphers are the following:
- Grain: ...
- HC-256: ...
- PANAMA: ...
- Rabbit: ...
- Rivest Cipher (RC4): It uses 64 or 128-bit long keys. It is used in TLS/SSL and IEEE 802.11 WLAN.
- Salsa20: ...
- Software-optimized Encryption Algorithm (SEAL): ...
- Scream: ...

&ensp;&ensp;&ensp; The block ciphers may differ in the block size which is a parameter that might be implementation specific. Here are some examples of such ciphers:
- 3DES
- Advanced Encryption Standard (AES): A cipher with 128-bit block length which uses 128, 192 or 256-bit symmetric key.
- Blowfish: ...
- Data Encryption Standard (DES): A 56-bit symmetric key cipher.
- Serpent: ...
- Twofish: A standard that uses Feistel networks. It uses blocks of 128 bits with key sizes from 128-bit to 256-bit.


## Objectives:
1. Get familiar with the symmetric cryptography, stream and block ciphers.

2. Implement an example of a stream cipher.

3. Implement an example of a block cipher.

4. The implementation should, ideally follow the abstraction/contract/interface used in the previous laboratory work.

5. Please use packages/directories to logically split the files that you will have.

6. As in the previous task, please use a client class or test classes to showcase the execution of your programs.

   
## Ciphers
1. [Stream Cipher](https://github.com/eugencic/utm-cs-labs/blob/main/Descriptions/Stream.md) 
2. [Block Cipher](https://github.com/eugencic/utm-cs-labs/blob/main/Descriptions/Block.md) 