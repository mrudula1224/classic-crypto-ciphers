
def caesar_cipher(text , shift):
    
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
              base = ord('A')
            else:
               base = ord('a')
            shifted = (ord(char) - base + shift)%26
            result += chr(shifted + base)
        elif char.isdigit():
            shifted = (ord(char) - ord('0') + shift)%10
            result += chr(shifted + ord('0'))  

        else:   
            result += char   

    return result 

def caesar_cipher_left(text , shift):
    
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
              base = ord('A')
            else:
               base = ord('a')
            shifted = (ord(char) - base + shift)%26
            result += chr(shifted + base)
        elif char.isdigit():
            shifted = (ord(char) - ord('0') + shift)%10
            result += chr(shifted + ord('0'))  
        else:   
            result += char   

    return result

print(caesar_cipher("STD12345", 5))
print(caesar_cipher("XYI67890", -5))
print(caesar_cipher_left("LOCKER123", 4))

