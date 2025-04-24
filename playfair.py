def generate_key_matrix(key):
    key = key.upper().replace("J","I").replace(" ","")
    matrix = []
    visited = set()


    for char in key:
        if char not in visited and char.isalpha():
            visited.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in visited:
            matrix.append(char)
            visited.add(char)

    return [ matrix[i:i+5] for i in range(0,25,5)]


def transform(text):
    text= text.upper().replace("J","I").replace(" ","")
    transformed = ""

    i = 0

    while i<len(text):
        a = text[i]
        b = text[i+1] if i+1<len(text) else 'X'

        if a == b:
            transformed += a + "X"
            i+=1 
        else:
            transformed += a+b 
            i+=2 

    if len(transformed)%2 !=0:
        transformed += 'X'
    return transformed


def find_position(matrix , char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i,j

    return None 

def find_encrypted_pair(a,b,matrix):
    row1 , col1 = find_position(matrix , a)
    row2, col2 = find_position(matrix , b)

    if row1 == row2:
        return matrix[row1][(col1+1)%5]+matrix[row2][(col2+1)%5]
    elif col1 == col2:
        return matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(text , key):
    matrix = generate_key_matrix(key)
    text = transform(text)
    encyrpyted = ""
    for i in range(0 , len(text) , 2):
        encyrpyted  += find_encrypted_pair(text[i],text[i+1],matrix)
    return encyrpyted

def find_decrypted_pair(a,b,matrix):
    row1 , col1 = find_position(matrix , a)
    row2, col2 = find_position(matrix , b)

    if row1 == row2:
        return matrix[row1][(col1-1)%5]+matrix[row2][(col2-1)%5]
    elif col1 == col2:
        return matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
    
def playfair_decrypt(cipher , key):
    matrix = generate_key_matrix(key)
    decrypt = ""
    for i in range(0 , len(cipher) , 2):
        decrypt += find_decrypted_pair(cipher[i],cipher[i+1],matrix)
    return decrypt

key = "MRUDULA"
plain_text = "SANIKA"

print(playfair_encrypt(plain_text , key))
print(playfair_decrypt("DASNJLRS" , key ))

final_text = playfair_decrypt("DASNJLRS" , key )
temp = final_text.replace('X',"")
print(temp)