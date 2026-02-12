import pandas as pd
laptops = pd.read_csv("laptops.csv", encoding="latin1")
laptops.info()


new_columns = []
for i in laptops.columns:
    clean_i = i.strip()
    new_columns.append(clean_i)
    
laptops.columns = new_columns  






gpu_split = laptops["gpu"].str.split()
laptops["gpu_manufacturer"] = gpu_split.str[0]
gpu_manufacturer_counts = laptops["gpu_manufacturer"].value_counts()


laptops["cpu_manufacturer"] =laptops["cpu"].str.split().str[0]
cpu_manufacturer_counts =  laptops["cpu_manufacturer"].value_counts()
