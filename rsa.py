# RSA Algorithm

from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public key e: "))

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    print("e must be coprime with phi(n)")
    exit()

d = mod_inverse(e, phi)

print("\nPublic Key  :", (e, n))
print("Private Key :", (d, n))

msg = int(input("\nEnter message (number): "))

cipher = pow(msg, e, n)
print("Encrypted Message:", cipher)

plain = pow(cipher, d, n)
print("Decrypted Message:", plain)