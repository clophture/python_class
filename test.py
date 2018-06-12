#!/usr/bin//env python3
gender = "MALE"


import json
with open('apft_chart.json', 'r') as f:
    chart_dict = json.load(f)




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

pushupRAW = str(inputPushup("How many pushups did you do? \n"))


print(chart_dict[gender]['run']['17_21'][pushupRAW])
