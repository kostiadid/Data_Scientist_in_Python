opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


data_sizes = []
for i in  apps_data[1:]:
    size = float(i[2])
    data_sizes.append(size)
    
min_size = min(data_sizes)
max_size = max(data_sizes)
