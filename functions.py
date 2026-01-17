# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)


def freq_table(some_list):
    dictionary = {}
    for i in some_list:
        if i in  dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    return dictionary
genres_ft=freq_table(genres)
