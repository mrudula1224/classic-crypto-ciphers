def text_to_vector(text):
    return [ord(char) - ord('A') for char in text.upper()]

def vector_to_text(vec):
    return ''.join([chr(int(num) + ord('A')) for num in vec])

# Hill Cipher Encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    result = ''
    for i in range(0, len(plaintext), 2):
        pair = text_to_vector(plaintext[i:i+2])
        vector = np.dot(key_matrix, pair) % 26
        result += vector_to_text(vector)

    return result

print("Enter 2x2 key matrix (4 integers):")
key_values = []
for i in range(4):
    val = int(input(f"Enter value {i+1}: "))
    key_values.append(val)

key_matrix = np.array(key_values).reshape(2, 2)

plaintext = input("Enter plaintext (letters only): ")


ciphertext = hill_encrypt(plaintext, key_matrix)
