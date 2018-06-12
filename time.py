#!/usr/bin//env python3


import json
with open('apft_chart.json', 'r') as f:
    chart_dict = json.load(f)

gender = "MALE"
m = int(input("enter minutes: "))
s = int(input("enter seconds: "))

total = m * 60 + s
remainder = total % 6
scoretime = total - remainder
m = (scoretime // 60)
s = (scoretime % 60 )
evaltime= str(m) + str(s).zfill(2)

print(total)
print(remainder)
print(scoretime)
print(m)
print(s)

evaltime= str(m) + str(s).zfill(2)

print(str(evaltime))

print(chart_dict[gender]['run']['17_21'][evaltime])
