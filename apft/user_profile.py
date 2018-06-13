#!/usr/bin//env python3

def inputProfile(message):
    """Prompt user for a 'YES' 'NO' if they have a profile"""
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
            return 'NO' if userInput.upper() in ('N', 'NO') else 'YES'
            break

def inputAltAerobic(message):
    """Prompt user for a '1' '2' '3' '4' to select which Alterante aerobic event they take"""
    while True:
        try:
            userInput = input(message)
        except ValueError:
            print("blah")
            continue
        else:
            if userInput.isalpha():
                print("You entered a string! Try again.")
                continue
            elif userInput.isdigit() not in (1, 2, 3, 4):
                print("Unrecognized input! Try again.")
                continue
            else:
                if userInput.isdigit() == 1:
                    return "walk" 
                elif userInput.isdigit() == 2:
                    return "cycle"
                elif userInput.isdigit() in 3:
                    return "cycle" 
                else:
                    return "swim"
                    break


def main():
    """Testing user input for profiles"""
    profile = inputProfile("Do you have a profile: [YES or NO] \n")
    aerobic = inputAltAerobic("Select the number of which alterante event you take \n1. Walk, 2. Stationary-Cycle Ergometer, 3. Bicycle, 4. Swim: \n")    
    run_profile = inputProfile("Is your profile for the run event: [YES or NO] \n")
    other_profile = inputProfile("Do you have another profile: [YES or NO] \n")
    pushup_profile = inputProfile("Is your profile for the pushup event: [YES or NO] \n")
    situp_profile = inputProfile("Is your profile for the situp event: [YES or NO] \n")


if __name__ == "__main__":
    main()
