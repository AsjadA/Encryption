def Encrypt():
    key = int(input("Enter the key for Encryption: " )) 
    string = input("Enter the string to encrypt: ")
    newstring = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    back=""
    for r in range(1,key+1):
        back=back+alpha[-r]
    for i in range(0, len(string)):
        if string[i] != " " and string[i] not in back:
            currentletter = ord(string[i])
            newletter = chr(currentletter + key)
            newstring.append(newletter)
                    
        elif string[i] in back:
            a = (ord(string[i]) - ord(alpha[-key]) + ord("A")) 
            b = chr(a)
            newstring.append(b)
        else:
            newstring.append(" ")
        #print(newstring)
    temp=""
    for j in range(0, len(newstring)):
        temp=temp+newstring[j]
    print(temp)

Encrypt()