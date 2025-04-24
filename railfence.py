def railfenceencrypt(plaintext , numrail):
    fence = [['' for _ in range(len(plaintext))] for _ in range(numrail)]
    rail = 0
    down = True 

    for i in range(len(plaintext)):
        fence[rail][i] = plaintext[i]
        if down:
            rail += 1
        else:
            rail -= 1
        
        if rail == numrail - 1:
            down = False 
        elif rail == 0:
            down = True 
    
    ciphertext = ""
    for row in fence:
        ciphertext += "".join(row)
    
    ciphertext = ciphertext.replace(" ","")
    return ciphertext



print(railfenceencrypt("MRUDULA",2))


def railfencedecryption(ciphertext , numrail):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(numrail)]
    down = True 
    rail = 0 
    index = 0

    for i in range(len(ciphertext)):
        fence[rail][i] = "*"
        if down:
            rail += 1
        else:
            rail -= 1
        if rail == numrail - 1:
            down = False 
        elif rail == 0:
            down = True 
    
    for row in fence:
        for i in range(len(row)):
            if row[i]=="*":
                row[i] = ciphertext[index]
                index += 1
    
    plaintext = ""
    down = True 
    rail = 0 

    for i in range(len(ciphertext)):
        plaintext += fence[rail][i]
        if down:
            rail += 1
        else:
            rail -= 1
        
        if rail == numrail - 1:
            down = False 
        elif rail == 0:
            down = True
    
    return plaintext

print(railfencedecryption("MUUARDL",2))




    