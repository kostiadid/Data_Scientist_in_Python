import pandas as pd
laptops = pd.read_csv("laptops.csv", encoding="latin1")
laptops.info()


new_columns = []
for i in laptops.columns:
    clean_i = i.strip()
    new_columns.append(clean_i)
    
laptops.columns = new_columns  


