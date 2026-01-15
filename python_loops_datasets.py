opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


apps_data[0].append('price_label')

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0:
        app.append('free')
    if price >0 and  price < 20:
        app.append('affordable')
    if price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append("very expensive")
    
