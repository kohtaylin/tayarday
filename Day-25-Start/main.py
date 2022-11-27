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
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temperature = sum(temp_list)/len(temp_list)
# print(average_temperature)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# maximum_temperature = data["temp"].max()
# print(maximum_temperature)

# # Get data in Columns
#
# print(data["temp"])
# print(data.temp)
#
# # Get data in Row
#
# print(data[data.day == "Monday"])

# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)

# monday = data[data.day == "Monday"]
# print(monday)

# # F = (C * 9/5) + 32
# mon_temp_C = data[data.day == "Monday"].temp
# mon_temp_F = (mon_temp_C * (9/5)) + 32
# print(mon_temp_F)

# Create a dataframe from scratch

dat_dict = {
    "students": ["Htay", "Lin", "Aung"],
    "score": [60, 70, 80]
}

dat = pandas.DataFrame(dat_dict)
dat.to_csv("new_dat.csv")
