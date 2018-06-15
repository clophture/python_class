#!/usr/bin//env python3
import os
import string
import random

def inputLen(message):
    """Prompt user for thier password length. userInput must be >= 14."""
    while True:
        try:
            userInput = int(input(message))
        except TypeError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput < 14:
                os.system('clear')
                print("Password must be 14 or greater! Try again.")
                continue
            elif userInput > 40:
                os.system('clear')
                print("You are not going to remember this! Try again.")
                continue
            else:
                return userInput
                break
def lowercase():
    """Print a random lowercase letter"""
    return random.choice(string.ascii_lowercase)

def uppercase():
    """Print a random uppercase letter"""
    return random.choice(string.ascii_uppercase)

def digit():
    """Print a random digit letter"""
    return random.choice(string.digits)

def punctuation():
    """Print a random punctuation letter"""
    return random.choice(string.punctuation)


def inputGen(message=14):
    print("pass")
    os.system('clear')
    p = []
    f = [lowercase, uppercase, digit, punctuation]
    userInput = int(input(message))
    for x in range(userInput):
        if len(p) < 3:
            p.append(random.choice(f)())
            ++x
        else:
           if p[-3].islower() and p[-2].islower() and p[-1].islower():
               p.append(random.choice([uppercase, digit, punctuation])())
               ++x
           elif p[-3].isupper() and p[-2].isupper() and p[-1].isupper():
               p.append(random.choice([lowercase, digit, punctuation])())
               ++x
           elif p[-3].isdigit() and p[-2].isdigit() and p[-1].isdigit():
               p.append(random.choice([lowercase, uppercase, punctuation])())
               ++x
           elif p[-3] in string.punctuation and p[-2] in string.punctuation and p[-1] in string.punctuation:
               p.append(random.choice([lowercase, uppercase, digit])())
               ++x
           else:
               p.append(random.choice(f)())
               ++x

    return (''.join(p))


def main():
    length = inputGen("How long of a password do you want? \n")
    print(length)


if __name__ == "__main__":
    main()
