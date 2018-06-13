#!/usr/bin//env python3
import json
with open('apft_chart.json', 'r') as f:
    chart_dict = json.load(f)


def evalPushup(pushupRAW,gender,age_group):
    """ Return the score for the amount of pushups completed for your age groupself.
    Expecting three arguments pushupRaw, gender, age_group. """
    if pushupRAW > 77:
        pushupScore = 100
        return pushupScore
    elif pushupRAW < 0:
        pushupScore = 0
        return pushupScore
    else:
        pushupScore = int(chart_dict[gender]['pushups'][age_group][str(pushupRAW)])
        return pushupScore

def evalSitup(situpRAW,gender,age_group):
    """ Return the score for the amount of Situps completed for your age groupself.
        Expecting three arguments situpRaw, gender, age_group. """
    if situpRAW > 82:
        situpScore = 100
        return situpScore
    elif situpRAW < 21:
        situpScore = 0
        return situpScore
    else:
        situpScore = int(chart_dict[gender]['situps'][age_group][str(situpRAW)])
        return situpScore

def evalRun(evaltime,gender,age_group):
    """ Return the score for run time completed for your age groupself.
        Expecting three arguments evaltime, gender, age_group. """
    if int(evaltime) < 1300:
        runScore = 100
        return runScore
    elif int(evaltime) > 2500:
        runScore = 0
        return runScore
    else:
        runScore = int(chart_dict[gender]['run'][age_group][str(evaltime)])
        return runScore

def main():
  pushupScore = evalPushup(45,"MALE","32_36")
  situpScore = evalSitup(45,"MALE","32_36")
  runScore = evalRun(1536,"MALE","32_36")
  print(pushupScore)
  print(situpScore)


if __name__ == "__main__":
    main()
