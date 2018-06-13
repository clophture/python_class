#!/usr/bin//env python3

def inputGender(message):
    """Prompt user for thier gender. userInput must be 'M', 'F', 'MALE', 'FEMALE'."""
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


def inputAge(message):
    """Prompt user for thier age. userInput must be >= 17. Output of function will return the
    year group individual will be evaluated against"""
    while True:
        try:
            userInput = int(input(message))
        except TypeError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput < 17:
                print("You need to be 17 or older be scored on the APFT! Try again.")
                continue
            if userInput < 22:
                age_group = "17_21"
                return age_group
            elif userInput > 21 and userInput < 27:
                age_group = "22_26"
                return age_group
            elif userInput > 26 and userInput < 32:
                age_group = "27_31"
                return age_group
            elif userInput > 31 and userInput < 37:
                age_group = "32_36"
                return age_group
            elif userInput > 36 and userInput < 42:
                age_group = "37_41"
                return age_group
            elif userInput > 41 and userInput < 47:
                age_group = "42_46"
                return age_group
            elif userInput > 46 and userInput < 52:
                age_group = "47_51"
                return age_group
            elif userInput > 51 and userInput < 57:
                age_group = "52_56"
                return age_group
            elif userInput > 56 and userInput < 62:
                age_group = "57_61"
                return age_group
            else:
                age_group = "62+"
                return age_group
            return userInput
            break

def main():
    """Testing user input for gender and age"""
    gender = inputGender("What is your gender? Male or Female: \n")
    age_group = inputAge("How old are you? \n")
    print(gender)
    print(age_group)

if __name__ == "__main__":
    main()
