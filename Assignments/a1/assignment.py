# Cipher

MAX_VALUE_SIZE = 25

def getChoice():
    while True:
        choice = input("Please choose an option [e/d/a/q]: \n e) Encrypt some text \n d) Decrypt some text\n a) Automatically decrypt English text\n q) Quit").lower()
        if choice == e:
            word = input(getWordEncrypt())
        elif choice == d:
            word = input(getWordDecrypt())
        elif choice == a:
            print('Bye!')
        elif choice == q:
            print('Bye!')
        else:
            print('Invalid command')

def getWordEncrypt():
    print('Please enter some text to encrypt: ')
    return input()

def getWordDecrypt():
    print('Please enter some text to decrypt: ')
    return input()

def getValue():
    Value = 0
    while True:
        print('Please enter a shift offset (1-25):' % (MAX_VALUE_SIZE))
        value = int(input())
        if (value >= 1 and value <= MAX_VALUE_SIZE):
            return value

def getTranslatedWord(choice, word, value):
    if word[0] == 'd':
        key = -key
    translated = ''

    for symbol in word:
        if symbol.isalpha():
            num = ord(symbol)
            num += value

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 25
                elif num < ord('A'):
                    num += 25
            elif symbol.islower():
                if num > ord('z'):
                    num -= 25
                elif num < ord('a'):
                    num += 25
                translated += chr(num)
        else:
            translated += symbol
        return translated
choice = getChoice()
word = getWord()
value = getValue()

print('The decrypted text is:')

print(getTranslatedMessage(choice, word, value))
