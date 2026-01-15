opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = []
for row in  apps_data[1:]:
    rating = float(row[7])
    rating_sum.append(rating)
    
avg_rating = sum(rating_sum) / (len(apps_data)-1)
print(avg_rating)
