opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def freq_table(column_num,data):
    column_list = []
    freq_dict = {}
    for i in data[1:]:
        column_list.append(i[column_num])
    for i in  column_list:
        if i in  freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i]=1
    return  freq_dict
    
    
ratings_ft=freq_table(7,apps_data)    
    
        
        
        
        
    
