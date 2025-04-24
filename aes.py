from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  
cipher = AES.new(key, AES.MODE_CBC)
data = b"Hello"

ciphertext = cipher.encrypt(pad(data, AES.block_size))
print(ciphertext)

decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)
print(plaintext)


