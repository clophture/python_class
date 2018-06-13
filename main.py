#!/usr/bin//env python3
import user_info
import user_raw
import eval_score
import cowsay


def main():
    gender = user_info.inputGender("What is your gender: Male or Female? \n")
    age_group = user_info.inputAge("How old are you? \n")
    pushupRAW = user_raw.inputPushup("How many pushups did you do? \n")
    situpRAW = user_raw.inputSitup("How many situps did you do? \n")
    evaltime = user_raw.inputRun("enter time [16:36]: \n")

    pushupScore = str(eval_score.evalPushup(pushupRAW,gender,age_group))
    situpScore = str(eval_score.evalSitup(situpRAW,gender,age_group))
    runScore = str(eval_score.evalRun(evaltime,gender,age_group))
    total = int(pushupScore) + int(situpScore) + int(runScore)
    cowsay.dragon("Your pushup score is " + pushupScore + "\n Your situp score is " + situpScore + "\n Your run score is " + runScore + "\n You total score is " + str(total))



if __name__ == "__main__":
    main()
