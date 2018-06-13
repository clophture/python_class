#!/usr/bin//env python3
import user_info
import user_profile
import user_raw
import eval_score
import cowsay



def main():
    gender = user_info.inputGender("What is your gender: Male or Female? \n")
    age_group = user_info.inputAge("How old are you? \n")


    profile = user_profile.inputProfile("Do you have a profile: [YES or NO] \n")
    if profile == "YES":
        run_profile = user_profile.inputProfile("Is your profile for the run event: [YES or NO] \n")
        if run_profile == "YES":
            aerobic = user_profile.inputAltAerobic("Select the number of which alterante event you take \n1. Walk, 2. Stationary-Cycle Ergometer, 3. Bicycle, 4. Swim: \n")
            other_profile = user_profile.inputProfile("Do you have another profile: [YES or NO] \n")
            if other_profile == "YES":
                pushup_profile = user_profile.inputProfile("Is your profile for the pushup event: [YES or NO] \n")
                situp_profile = user_profile.inputProfile("Is your profile for the situp event: [YES or NO] \n")
            else:
                pushup_profile = "NO"
                situp_profile = "NO"
        else:
            pushup_profile = user_profile.inputProfile("Is your profile for the pushup event: [YES or NO] \n")
            situp_profile = user_profile.inputProfile("Is your profile for the situp event: [YES or NO] \n")
            run_profile = "NO"
            aerobic = "run"
    else:
        pushup_profile = "NO"
        situp_profile = "NO"
        run_profile = "NO"
        aerobic = "run"

    if pushup_profile == "YES":
        pushupScore = "60"
    else:
        pushupRAW = user_raw.inputPushup("How many pushups did you do? \n")
        pushupScore = str(eval_score.evalPushup(pushupRAW,gender,age_group))
    
    if situp_profile == "YES":
        situpScore = "60"
    else:
        situpRAW = user_raw.inputSitup("How many situps did you do? \n")
        situpScore = str(eval_score.evalSitup(situpRAW,gender,age_group))    



    evaltime = user_raw.inputRun("enter time you completed the " + aerobic +" [16:36]: \n")
    aerobicScore = str(eval_score.evalAerobic(evaltime,gender,age_group,aerobic))



    total = int(pushupScore) + int(situpScore) + int(aerobicScore)
    cowsay.tux("Your pushup score is " + pushupScore + "\n Your situp score is " + situpScore + "\n Your run score is " + aerobicScore + "\n You total score is " + str(total))



if __name__ == "__main__":
    main()
