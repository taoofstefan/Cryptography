"""
RSA Encryption and Decryption (Number-based)
This code implements the RSA encryption and decryption algorithm using integer-based operations.
It allows for the encryption and decryption of numbers using a public-private key pair.

Usage
Set the values of prime numbers p and q in the code.
Run the code.
The public and private key pairs will be generated and displayed.
Enter a number between 0 and 221 as the message to be encrypted.
The message will be encrypted using the public key.
Enter the private key components (decrypt1 and decrypt2) for decryption.
The encrypted message will be decrypted using the private key and displayed.

Dependencies
Crypto.Util.number module from the Cryptography library.
"""
from Crypto.Util.number import inverse
# basic values
p = 13
q = 17
n = p * q
phi = (p - 1) * (q - 1)

# Generate and print public and private keys
e = 11
d = inverse(e, phi)
print("Public key: ({:d}, {:d})".format(e, n))
print("Private key: ({:d}, {:d})".format(d, n))

# message
message = int(input("input number between 0 and 221: "))

# encrypt
cypher = pow(message, e, n)

# decrypt
decrypt1 = int(input("Private key to decrytp part 1: "))
decrypt2 = int(input("Private key to decrytp part 2: "))

print(str(pow(cypher, decrypt1, decrypt2)))