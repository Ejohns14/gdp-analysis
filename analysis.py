import csv

def get_highest_gdp(data, year):
    highest_gdp_state = data[0]["GeoName"]
    maximum = float(data[0][year])
    for d in data:
        # if that value is greater than the max I've seen so far
        value = float(d[year])
        if value < maximum:
            continue
            # set it to be my new max
        if value > maximum:
            maximum = value
            highest_gdp_state = d["GeoName"]
    return highest_gdp_state


def get_lowest_gdp(data, year):
    lowest_gdp_state = data[0]["GeoName"]
    minimum = float(data[0][year])
    for d in data:
        # if that value is greater than the max I've seen so far
        value = float(d[year])
        if value > minimum:
            continue
            # set it to be my new max
        if value < minimum:
            minimum = value
            lowest_gdp_state = d["GeoName"]
        return lowest_gdp_state

def get_state_gdp(data, state, year):
    for row in data:
        if row["GeoName"] == state:
            return row[year]
        
    
# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))
