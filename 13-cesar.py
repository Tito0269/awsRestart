def getDoubleAphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    while True:
        stringToEncrypt = input("Please enter a message to encrypt: ")
        if bool(stringToEncrypt):
            return stringToEncrypt
        else:
            continue
    
def getCipherKey():
    while True:
        shiftAmount = input("Please enter a key (whole number from 1-25): ")
        if bool(shiftAmount) and shiftAmount.isnumeric() and 1 <= int(shiftAmount) <= 25:
             return shiftAmount
        else:
            continue    
"""
        if bool(shiftAmount):
            elif :
                print("Ingrese un Numero: ")
            if shiftAmount.isnumeric():
                if 1 <= int(shiftAmount) <= 25:
                    return shiftAmount
        else:
            continue
"""  
    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()