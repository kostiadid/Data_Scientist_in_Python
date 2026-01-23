
import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for element in row:
        converted_row.append(float(element))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment

taxi = np.array(converted_taxi_list)


# As I understand it, Python helps us speed up work with data structures by executing several identical processes simultaneously, 
#which is called vectorization. As I understand it, if we simply iterated over a list of lists in pure Python, 
#it would require twice as many CPU cycles, but if we iterate over an array using Python, it will take half as many ticks.

