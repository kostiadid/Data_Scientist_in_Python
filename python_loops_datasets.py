from csv import reader

opened_file = open('AppleStore.csv')


read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))


rating_sum = 0

for  row  in apps_data[1:] : 
    rating = float(row[7])
    rating_sum+=rating
    
avg_rating = rating_sum / (len(apps_data)-1)
    
