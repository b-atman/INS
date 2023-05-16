import hashlib
import math
from math import gcd

p = 13
q = 27

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break
j = 0
while True:
    if (j * e) % phi == 1:
        d = j
        break
    j += 1

# Convert the message to a hash value
message = b"This is the plain text"
hash_value = hashlib.sha256(message).hexdigest()
hash_value = int(hash_value, 16) % n
print("original hash:", hash_value)

signature = pow(hash_value, d, n)
print("Digital Signature : ", signature)

# Verify the signature
hash_value_check = pow(signature, e, n)
print("Hashed Digest : ", hash_value_check)

if hash_value_check == hash_value:
    print("Signature is valid for the given input")
else:
    print("Signature is invalid for the given input")
