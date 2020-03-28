#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Daniel Zhang & 45004830"

# Write your functions here


def encrypt(text,offset):
    """etext means encrypted_text
       echar means encrypted_char
    """
    etext=""
    for char in text:
        if is_english_character(char):
            num = ord(char) + offset
            if num > ord('z'):
                num = ord('a') + num - ord('z') - 1
            if num > ord('Z') and ord(char) <= ord('Z'):
                num = ord('A') + num - ord('Z') - 1
            echar = chr(num)

            etext += echar
        else:
            etext += char
    return etext

def is_english_character(char):
    """ To define whether the charater is a english character
    """
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return True
    elif ord(char) >= ord('a') and ord(char) <= ord('z'):
        return True
    else:
        return False

def decrypt(etext,offset):
    """dtext means decrypted_text
       dchar means decrypted_char
    """
    dtext=""
    for char in etext:
        if is_english_character(char):
            num = ord(char)-offset
            if num < ord('A'):
                num = ord('Z') + num - ord('A') + 1
            elif num < ord('a') and ord(char) >= ord('a'):
                num = ord('z') + num - ord('a') + 1

            dchar = chr(num)
            dtext += dchar
        else:
            dtext += char
    return dtext

def find_encryption_offsets(encrypted_text):
    word_list = encrypted_text.split(' ')
    for word in word_list:
        count = 0
        for char in word:
            if is_english_character(char):
                count += 1
            if len(word) == count:
                break

    offset_list = []
    for offset in range(1,26):
        dword = decrypt(word,offset)
        if is_word_english(dword):
            offset_list.append(offset)        

    return tuple(offset_list)


def main():
    # Add your main code here
    while True:
        print("Please choose an option [e/d/a/q]: \n e) Encrypt some text \n d) Decrypt some text\n a) Automatically decrypt English text\n q) Quit")
        choice = input('>')
        if choice == 'e':
            text = input("Please enter some text to encrypt:")
            offset = int(input("Please enter a shift offset (1-25):"))
            if offset == '0':
                for loop in range(1,26):
                    etext = encrypt(text,loop)
                    print("The encrypted text is:" + etext)
            else:
                etext = encrypt(text,offset)
                print("The encrypted text is:" + etext)
        elif choice == 'd':
            text = input("Please enter some text to decrypt:")
            offset = int(input("Please enter a shift offset (1-25):"))
            dtext = decrypt(text,offset)
            print("The decrypted text is:" + dtext)
        elif choice == 'a':
            text = input("Please enter some text to encrypt:")
            offset_tuple = find_encryption_offsets(etext)
            if offset_tuple == ():
                print("No valid encryption offset")
                continue
            elif len(offset_tuple)!= 1:
                print("Multiple encryption offsets:", offset_tuple)
            else:
                dtext = decrypt(etext,offset_tuple[0])
                print("Encryption offset:", offset_tuple[0])
                print("Decrypted message:" + dtext)
        elif choice == 'q':
            print('Bye!')
            break
        else:
            print('Invalid command')
    pass

  
##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

