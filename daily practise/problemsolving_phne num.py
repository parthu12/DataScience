def isPhoneNumber(message):
    if len(message)!=12:
        return False
    for i in range(0,3):
        if not message[i].isdecimal():
            return False
    if message[3] != '-':
        return False
    for i in range(4,7):
        if not message[i].isdecimal():
            return False
    if message[7] != '-':
        return False
    for i in range(8,12):
        if not message[i].isdecimal():
            return False
    return True
print(isPhoneNumber('880-334-4567'))
print(isPhoneNumber('88-334-4567'))

inputString = "This is a message with a phone num :880-334-4567"
for i in range(0,len(inputString)):
    chuck = inputString[i:i+12]
    if isPhoneNumber(chuck):
        print(chuck)
    
    

    
