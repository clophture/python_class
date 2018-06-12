#!/usr/bin//env python3
gender = "male"


import json
with open('apft_chart.json', 'r') as f:
    chart_dict = json.load(f)

print(chart_dict[gender]['pushups']['17_21']['70'])
