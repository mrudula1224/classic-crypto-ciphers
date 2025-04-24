from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# DES uses 8 byte keys
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CBC)
data = b'Hello DES!'
ciphertext = cipher.encrypt(pad(data, DES.block_size))

# Decryption
decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("\nDES:")
print("Key:", key)
print("IV:", cipher.iv)
print("Encrypted:", ciphertext)
print("plaintext:", plaintext)