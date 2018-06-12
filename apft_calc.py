#!/usr/bin//env python3

import json

def inputAge(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput < 17:
                print("You need to be 17 or older be scored on the APFT! Try again.")
                continue
            return userInput
            break

def setAgeGroup():
    global age
    if age < 22:
        age_group = "17_21"
        return age_group
    elif age > 21 and age < 27:
        age_group = "22_26"
        return age_group
    elif age > 26 and age < 32:
        age_group = "27_31"
        return age_group
    elif age > 31 and age < 37:
        age_group = "32_36"
        return age_group
    elif age > 36 and age < 42:
        age_group = "37_41"
        return age_group
    elif age > 41 and age < 47:
        age_group = "42_46"
        return age_group
    elif age > 46 and age < 52:
        age_group = "47_51"
        return age_group
    elif age > 51 and age < 57
        age_group = "52_56"
        return age_group
    elif age > 56 and age < 62
        age_group = "57_61"
        return age_group
    else:
        age_group = "62+"
        return age_group


def inputGender(message):
    while True:
        try:
            userInput = input(message)
        except ValueError:
            print("blah")
            continue
        else:
            if userInput.isdigit():
                print("You entered a number! Try again.")
                continue
            elif userInput.upper() not in ('M', 'F', 'MALE', 'FEMALE'):
                print("Unrecognized input! Try again.")
                continue
            return 'MALE' if userInput.upper() in ('M', 'MALE') else 'FEMALE'
            break

def inputPushup(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break

def inputSitup(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break

def inputRunM(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break

def inputRunS(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


def inputProfile(message):
    while True:
        try:
            userInput = input(message)
        except ValueError:
            print("blah")
            continue
        else:
            if userInput.isdigit():
                print("You entered a number! Try again.")
                continue
            elif userInput.upper() not in ('Y', 'N', 'YES', 'NO'):
                print("Unrecognized input! Try again.")
                continue
            return 'YES' if userInput.upper() in ('Y', 'YES') else 'NO'
            break





gender = inputGender("What is your gender: Male or Female? \n")

age = inputAge("How old are you? \n")
age_group = setAgeGroup()

#profile = inputProfile("Do you have a profile? \n")

pushupRAW = inputPushup("How many pushups did you do? \n")

situpRAW = inputSitup("How many situps did you do? \n")

runMRAW = inputRunM("How many minutes did you complete the 2 mile run in? \n")
runSRAW = inputRunS("How many seconds did you complete the 2 mile run in? \n")



print("\n\n")
print("You are a " + str(age) + " year old " + str(gender) + ".")
print("You completed " + str(pushupRAW) + " pushups & " + str(situpRAW) + " situps.")
print("You ran 2 miles in " + str(runMRAW) + ":" + str(runSRAW) + " minutes.")
#print("Your profile status is " + str(profile) + ".")
print("Your age group is " + str(age_group) +" \n")
