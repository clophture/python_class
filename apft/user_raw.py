#!/usr/bin//env python3

def inputPushup(message):
    """Prompt user for the amount of pushups they performed. userInput must
    int() and will return value for lookup in dictionary"""
    while True:
        try:
            userInput = int(input(message))
        except TypeError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput < 0:
                print("Enter a POSITIVE number! Try again.")
                continue
            return userInput
            break

def inputSitup(message):
    """Prompt user for the amount of situps they performed. userInput must
    int() and will return value for lookup in dictionary"""
    while True:
        try:
            userInput = int(input(message))
        except TypeError:
            print("Not an integer! Try again.")
            continue
        else:
            if userInput < 0:
                print("Enter a POSITIVE number! Try again.")
                continue
            return userInput
            break

def inputRun(message):
    """Prompt user for the time they completed the run in they performed. userInput must
    int() in MM:SS format and will return value for lookup in dictionary"""
    while True:
        try:
            m,s = map(int,input(message).split(':'))
        except TypeError:
            print("Not an integer! Try again.")
            continue
        else:
            total = m * 60 + s
            remainder = total % 6
            scoretime = total - remainder
            m,s = divmod(scoretime, 60)
            evaltime = '%02d%02d' % (m,s)
            return evaltime
            break


def main():
    """Testing user input for gender and age"""
    pushupRAW = inputPushup("How many pushups did you do? \n")
    situpRAW = inputSitup("How many situps did you do? \n")
    evaltime = inputRun("enter time [16:36]: \n")
    print(pushupRAW)
    print(situpRAW)
    print(evaltime)

if __name__ == "__main__":
    main()
