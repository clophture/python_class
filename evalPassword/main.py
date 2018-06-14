#!/usr/bin//env python3
import os
import string
import getpass
import random
import cowsay

def inputPass(message):
    """Prompt user for thier password. userInput will return."""
    while True:
        print("Enter a password with at least length of 14. Password must contain lowercase, \nuppercase, digits, and punctuation. You can not use more than three of the same time in a row.")
        password1 = getpass.getpass()
        password2 = getpass.getpass()
#        password1 = input("pass ")
#        password2 = input("pass ")
        if str(password1) == str(password2) and len(password1) > 13:
            return password1
            break
        else:
            os.system('clear')
            print("Passwords don't match or is too short! Try again.")
            continue

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def main():
    os.system('clear')
    password = inputPass("Enter you password? \n")
    p = list(password)
    for x in range(len(password)-2):
        if p[x-1].islower() and p[x].islower() and p[x+1].islower() and p[x+2].islower():
            os.system('clear')
            print("Password contains 4 lowercase in a row. Try again!\n")
            password = inputPass("Enter you password? \n")
        elif p[x-1].isupper() and p[x].isupper() and p[x+1].isupper() and p[x+2].isupper():
            os.system('clear')
            print("Password contains 4 uppercase in a row. Try again!\n")
            break
        elif p[x-1].isdigit() and p[x].isdigit() and p[x+1].isdigit() and p[x+2].isdigit():
            os.system('clear')
            print("Password contains 4 digits in a row. Try again!\n")
            break
        elif p[x-1] in string.punctuation and p[x] in string.punctuation and p[x+1] in string.punctuation and p[x+2] in string.punctuation:
            os.system('clear')
            print("Password contains 4 punctuation in a row. Try again!\n")
            break
        else:
            pass
    cowsay.daemon('{} \n your password is good!'.format(password))


if __name__ == "__main__":
    main()
