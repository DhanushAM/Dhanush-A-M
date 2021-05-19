

text = input('Enter A Cypher Text To show Decrypt Message\n')
            
move= 3

def encrypt(text,move):
    result = ""
 
  
    for i in range(len(text)):
        char = text[i]
 
       
 
        if (char.isupper()):
            result += chr((ord(char) + move- 65) % 26 + 65)
 
        
 
        else:
            result += chr((ord(char) + move- 97) % 26 + 97)
 
    return result
 

print ("Actual  : " + text)
print ("Shift : " + str(move))
print ("Encoded: " + encrypt(text,move))
