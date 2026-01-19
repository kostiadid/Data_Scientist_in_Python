opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table


content_ratings_ft = freq_table(apps_data , 10)
ratings_ft = freq_table(data_set = apps_data , index = 7)
genres_ft = freq_table(data_set = apps_data , index = 11)








# Parsing in strings 
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]



def strip_characters(string):
    for char in bad_chars:
        string=string.replace(char,"")
    return string
stripped_test_data =[]
for d in test_data:
    date = strip_characters(d)
    stripped_test_data.append(date)
