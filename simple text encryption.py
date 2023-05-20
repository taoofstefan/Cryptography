"""
RSA Encryption and Decryption (Text-based)
This code extends the RSA encryption and decryption algorithm to handle text-based messages.
It allows for the encryption and decryption of text using a public-private key pair.

Usage
Set the values of prime numbers p and q in the code.
Run the code.
The public and private key pairs will be generated and displayed.
Enter the text message to be encrypted.
The message will be converted to its numeric representation and encrypted using the public key.
The encrypted message will be displayed.
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
message = input("Enter the message to encrypt: ")

# Convert message to numeric representation
numeric_message = []
for char in message:
    numeric_message.append(ord(char))

# Encrypt
encrypted_message = []
for num in numeric_message:
    cypher = pow(num, e, n)
    encrypted_message.append(cypher)

# Decrypt
decrypted_message = ""
for cypher in encrypted_message:
    decrypted_num = pow(cypher, d, n)
    decrypted_char = chr(decrypted_num)
    decrypted_message += decrypted_char

print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)