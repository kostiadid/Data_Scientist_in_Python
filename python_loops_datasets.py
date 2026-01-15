opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_data[0].append('free_or_not')
for app in apps_data[1:]:
    price = float(app[4])
    if price:
        app.append("not free")
    else:
        app.append("free")
    

print(apps_data[:6])
    # Complete code from here
