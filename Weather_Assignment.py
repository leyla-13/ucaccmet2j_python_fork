# importing packages
import json

#opening data file with JSON
with open ('precipitation.json') as file:
    data = json.load(file)

# filtering for data from the seattle station

city_dat = [] # empty list to store seattle data
for entry in data:
    if entry['station'] == 'GHCND:US1WAKG0038':
        city_dat.append(entry) # filling the list with all the seattle data


# # Calculate the total_monthly_precipitation: a list with the total precipitation per month,
# for that location

total_monthly_precipitation = {} #creating an empty list to store month key and precipitation sum output

for entry in city_dat:
    grouping = entry['date'].split('-') #splitting from "-" so i can isolate the month, date is now a list of strings
    month = grouping[1]                 # taking the index 1 (so 2nd in list) item from the list
    if month not in total_monthly_precipitation:   #adding month to the dict. if i thasnt been recognized already
        total_monthly_precipitation[month] = 0
    total_monthly_precipitation[month] +=  entry['value'] # this being out of the if indent tells it to add it per month
                                                # and not just do it once when it recognizes the month and never again.

print(f'monthly precipitation sum is {total_monthly_precipitation}') #printing total precipitation per month

total_monthly_precipitation_list = (list(total_monthly_precipitation.values())) #converting the dictionary to a list


# # calculating yearly precipitation

total_year_precipitation = {} #creating an empty list to store month key and precipitation sum output

for entry in city_dat:
    yeargroup = entry['date'].split('-') #splitting from "-" so i can isolate the year, date is now a list of strings
    year = yeargroup[0]                 # taking the index 0 (so 1st in list) item from the list
    if year not in total_year_precipitation:   #adding year to the dict. if i thasnt been recognized already
        total_year_precipitation[year] = 0
    total_year_precipitation[year] +=  entry['value'] # this being out of the if indent tells it to add it per year
                                                # and not just do it once when it recognizes the year and never again.

print(f'this is the total years precipitation: {total_year_precipitation}') #printing total precipitation per year

total_year_precipitation_list = (list(total_year_precipitation.values())) #converting the dictionary to a list

# calculating relative monthly precipitation

relative_monthly = {}

for month in total_monthly_precipitation:
    relative_monthly[month] = total_monthly_precipitation[month] / total_year_precipitation['2010']

print(f'this is the relative monthly precipitation {relative_monthly}')

relative_monthly_precipitation_list = (list(relative_monthly.values())) #converting the dictionary to a list
print(relative_monthly_precipitation_list)

#storing data into the result JSON file
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
        "total_yearly_precipitation": [11180],
        "relative_monthly_precipitation": [0.15143112701252237, 0.06529516994633273, 0.0778175313059034, 0.06726296958855098, 0.08264758497316636, 0.053756708407871195, 0.00483005366726297, 0.009302325581395349, 0.089087656529517, 0.081216457960644, 0.10661896243291592, 0.2107334525939177],
        "relative_yearly_precipitation": []
        }

    }

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(part1dat, file, indent=4)

print(total_monthly_precipitation_list)
print(total_year_precipitation)
print(total_monthly_precipitation_list/ string_yearly)

print (month)

