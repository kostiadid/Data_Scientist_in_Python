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


# Dictionary and map for replasing incorect data 
os=laptops['os'].unique()

mapping_dict = {'Android': 'Android', 'Chrome OS': 'Chrome OS','Linux': 'Linux','Mac OS': 'macOS',  'No OS': 'No OS','Windows': 'Windows',  'macOS': 'macOS'}
laptops['os']= laptops['os'].map(mapping_dict)

osCounts = laptops["os"].value_counts()

#Dropping Missing Values
laptops_no_null_rows = laptops.dropna()
laptops_no_null_cols = laptops.dropna(axis=1)






value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

laptops.loc[laptops["os"] == "No OS","os_version"] = "Not Applicable"


value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()


