# Diffie-Hellman Key Exchange

q = int(input("Enter prime number q: "))
g = int(input("Enter primitive root g: "))

xa = int(input("Enter private key of A: "))
xb = int(input("Enter private key of B: "))

YA = pow(g, xa, q)
YB = pow(g, xb, q)

KA = pow(YB, xa, q)
KB = pow(YA, xb, q)

print("\nPublic Key of A (YA):", YA)
print("Public Key of B (YB):", YB)

print("\nShared Secret Key computed by A:", KA)
print("Shared Secret Key computed by B:", KB)