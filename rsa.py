def gcd(a, h):
    temp = 0
    while (1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp


p = int(input("Enter the value of p:"))  # 3
q = int(input("Enter the value of q:"))  # 7
n = p * q
e = 2
phi = (p - 1) * (q - 1)

while (e < phi):
    # e must be co-prime to phi and
    # smaller than phi.
    if (gcd(e, phi) == 1):
        break
    else:
        e = e + 1
print("e:", e)

d = 1
while (d * e) % phi != 1:
    d += 1
print("d:", d)
# Message to be encrypted
msg = int(input("Enter the message:"))  # 12.0

print("Message data = ", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n
m = pow(c, d, n)
print("Original Message Sent = ", m)
