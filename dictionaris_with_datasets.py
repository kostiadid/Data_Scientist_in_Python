opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


rating_list = []
for i in  apps_data[1:]:
    rating_list.append(float(i[5]))
    
max_val = max(rating_list)
min_val = min(rating_list)
avg_value = sum(rating_list) / len(rating_list)
intervals = {
    'min': 0,
    'before': 0,
    'avrg': 0,
    'after': 0,
    'max+': 0
}
for i in apps_data[1:]:
    val = float(i[5])
    if val <= 10000:
        intervals['min'] += 1
    elif 10000 < val <= 100000:
        intervals['before'] += 1
    elif 100000 < val <= 500000:
        intervals['avrg'] += 1
    elif 500000 < val <= 1000000:
        intervals['after'] += 1
    elif val > 1000000:
        intervals['max+'] += 1
        
print(intervals)
        

