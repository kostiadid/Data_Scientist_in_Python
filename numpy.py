
import csv
import numpy as np
import timeit

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



#Shape method
taxi_shape = taxi.shape
print(taxi_shape)

# list slower then   array for  loop operatrions ??  
lst = [[i for i in range(1000)] for _ in range(1000)]
arr = np.array(lst)

t_list = timeit.timeit(
    stmt="sum(sum(row) for row in lst)",
    globals=globals(),
    number=100
)

print("List:", t_list)

t_array = timeit.timeit(
    stmt="arr.sum()",
    globals=globals(),
    number=100
)

print("Array:", t_array)

#Selecting and Slicing Rows from Ndarrays
row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]


row_21_column_5 = taxi[21,5]


