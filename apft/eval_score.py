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

def evalAerobic(evaltime,gender,age_group,aerobic):
    """ Return the score for run time completed for your age groupself.
        Expecting four arguments evaltime, gender, age_group, aerobic. """
    if aerobic in ("walk", "cycle", "swim"): 
        if int(evaltime) <= int(list(sorted((chart_dict[gender][aerobic][age_group].keys())))[0]):
            aerobicScore = 60
            return aerobicScore
        else:
            aerobicScore = 0
            return aerobicScore
    elif int(evaltime) < int(list(sorted((chart_dict[gender][aerobic][age_group].keys())))[0]):
        aerobicScore = 100
        return aerobicScore
    elif int(evaltime) > int(list(sorted((chart_dict[gender][aerobic][age_group].keys())))[-1]):
        aerobicScore = 0
        return aerobicScore
    else:
        aerobicScore = int(chart_dict[gender][aerobic][age_group][str(evaltime)])
        return aerobicScore

def main():
  pushupScore = evalPushup(45,"MALE","32_36")
  situpScore = evalSitup(45,"MALE","32_36")
  aerobicScore = evalAerobic(1536,"MALE","32_36")
  print(pushupScore)
  print(situpScore)


if __name__ == "__main__":
    main()
