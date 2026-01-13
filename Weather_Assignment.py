# importing packages
import json

#opening data file with JSON
with open ('precipitation.json') as file:
    data = json.load(file)

# filtering for data from the seattle station

seattle_dat = [] # empty list to store seattle data
for entry in data:
    if entry['station'] == 'GHCND:US1WAKG0038':
        seattle_dat.append(entry) # filling the list with all the seattle data

print(seattle_dat[:10])

# Calculate the total_monthly_precipitation: a list with the total precipitation per month,
# for that location

total_monthly_precipitation = {}

for entry in seattle_dat:
    grouping = entry['date'].split('-')
    month = grouping[1]
    if month not in total_monthly_precipitation:
        total_monthly_precipitation[month] = 0
    total_monthly_precipitation[month] +=  entry['value'] # this being out of the if indent tells it to add it per month
                                                # and not just do it once when it recognizes the month and never again.



total_monthly_precipitation_list = (list(total_monthly_precipitation.values()))

part1dat = {
    "Cincinnati": {
        "station": "GHCND:USW00093814",
        "state": "OH",
        "total_monthly_precipitation": [],
        "total_yearly_precipitation": [],
        "relative_monthly_precipitation": [],
        "relative_yearly_precipitation": []
        },
    "Maui": {
        "station": "GHCND:USC00513317",
        "state": "HI",
        "total_monthly_precipitation": [],
        "total_yearly_precipitation": [],
        "relative_monthly_precipitation": [],
        "relative_yearly_precipitation": []
        },
    "Seattle": {
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": [1693, 730, 870, 752, 924, 601, 54, 104, 996, 908, 1192, 2356],
        "total_yearly_precipitation": [],
        "relative_monthly_precipitation": [],
        "relative_yearly_precipitation": []
        }

    }

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(part1dat, file, indent=4)

print(total_monthly_precipitation_list)
print (month)
print(total_monthly_precipitation)
