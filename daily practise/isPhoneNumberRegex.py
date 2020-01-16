import re

def isPhoneNumberRegex(message):
    phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchingObject =phoneRegex.search(message)
    result= str(matchingObject.group())
    return result

inputString = "This is a message with a phone num :880-334-4567"

print(isPhoneNumberRegex(inputString))

