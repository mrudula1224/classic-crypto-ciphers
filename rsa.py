import math

p = 3
q = 5

n = p * q
print("n =", n)

phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
print("e =", e)

d = pow(e, -1, phi)
print("d =", d)

print(f"Public key = ({e}, {n})")
print(f"Private key = ({d}, {n})")

msg = 8
c = pow(msg, e, n)
print("Ciphertext =", c)

M = pow(c, d, n)
print("Plaintext =", M)





