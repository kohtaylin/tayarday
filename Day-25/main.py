# with open("weather_data.csv") as dt:
#     data = dt.readlines()
#     print(data)

# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

import pandas


data = pandas.read_csv("weather_data.csv")
print(data["temp"])
