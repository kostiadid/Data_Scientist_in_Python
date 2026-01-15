opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
apps_greaterThen_9 = []


greaterThen = 0
less_orEuq = 0
for i in apps_data[1:]:
    rating = float(i[7])
    
    if float(i[4]) > 9:
        apps_greaterThen_9.append(rating)
        greaterThen+=1
    else :
        less_orEuq+=1
avg_rating = sum(apps_greaterThen_9) / greaterThen  

n_apps_more_9 = greaterThen
n_apps_less_9 = less_orEuq

