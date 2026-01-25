



import pandas as pd

# read the dataset into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
f500_selection = f500.loc[:,['rank','revenues','revenue_change']].head(5)




#Reading CSV Files with pandas
f500=pd.read_csv('f500.csv')

f500.index.name = "Company"
f500.columns.name = "Metric"


bool_0_f500 = f500["previous_rank"] == 0
f500.loc[bool_0_f500,'previous_rank'] = np.nan








