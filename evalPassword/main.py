#!/usr/bin//env python3
import os
import string
import getpass
import random
import cowsay
import re

def inputPass(message):
    """Prompt user for thier password. userInput will return."""
    while True:
        print("Enter a password with at least length of 14. Password must contain lowercase, \nuppercase, digits, and punctuation. You can not use more than three of the same time in a row.")
        password1 = getpass.getpass()
        password2 = getpass.getpass()
        if str(password1) == str(password2) and len(password1) > 13:
            return password1
            break
        else:
            os.system('clear')
            print("Passwords don't match or is too short! Try again.")
            continue





def hasLower(password):
#    print("hasLower()") 
    return any(char.islower() for char in password)

def hasUpper(password):
#    print("hasUpper()") 
    return any(char.isupper() for char in password)

def hasDigit(password):
#    print("hasDigit") 
    return any(char.isdigit() for char in password)

def hasPunc(password):
    t = password
    punc = list(string.punctuation)
#    print("hasPunc()") 
    return any(x in punc for x in t)

def hasSpace(password):
    return any(char.isspace() for char in password)

def CheckPass(t):
    password = t
    print(password)
    p = list(password)
 #   print(p)
    if len(password) < 14:
        return False
    elif hasLower(password) is False:
        return False
    elif hasUpper(password) is False:
        return False
    elif hasDigit(password) is False:
        return False
    elif hasPunc(password) is False:
        return False
    elif hasSpace(password) is True:
        return False
    else:
        for x in range(len(password)):
            print(x)
#            print(len(password))
            if x < 4:
                ++x
            elif p[x-4].islower() and p[x-3].islower() and p[x-2].islower() and p[x-1].islower():
                #print(p + "islower")
#                print(False)
                return False
#                break
            elif p[x-4].isupper() and p[x-3].isupper() and p[x-2].isupper() and p[x-1].isupper():
#                print(p + "isupper")
                return False
#                break
            elif p[x-4].isdigit() and p[x-3].isdigit() and p[x-2].isdigit() and p[x-1].isdigit():
#                print(p + "isdigit")
                return False
#                break
            elif p[x-4] in string.punctuation and p[x-3] in string.punctuation and p[x-2] in string.punctuation and p[x-1] in string.punctuation:
#                print(p + "ispunc")
                return False
#                break
            elif x < (len(password)):
                print(p)
                ++x
            elif x == (len(password)):
                return True
            else:
                #print(x+2)
                print('True')
        return True

#def main():

    # os.system('clear')
    # password = inputPass("Enter you password? \n")
    # p = list(password)
    # for x in range(len(password)-2):
    #     if p[x-1].islower() and p[x].islower() and p[x+1].islower() and p[x+2].islower():
    #         os.system('clear')
    #         print("Password contains 4 lowercase in a row. Try again!\n")
    #         password = inputPass("Enter you password? \n")
    #     elif p[x-1].isupper() and p[x].isupper() and p[x+1].isupper() and p[x+2].isupper():
    #         os.system('clear')
    #         print("Password contains 4 uppercase in a row. Try again!\n")
    #         break
    #     elif p[x-1].isdigit() and p[x].isdigit() and p[x+1].isdigit() and p[x+2].isdigit():
    #         os.system('clear')
    #         print("Password contains 4 digits in a row. Try again!\n")
    #         break
    #     elif p[x-1] in string.punctuation and p[x] in string.punctuation and p[x+1] in string.punctuation and p[x+2] in string.punctuation:
    #         os.system('clear')
    #         print("Password contains 4 punctuation in a row. Try again!\n")
    #         break
    #     else:
    #         pass
    # cowsay.daemon('{} \n your password is good!'.format(password))


#if __name__ == "__main__":
 #   main()
