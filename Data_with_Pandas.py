import pandas as pd

f500 = pd.read_csv("f500.csv")

f500_head = f500.head(10)
print(f500.info())



#Vectorized Operations
rank_change = f500['previous_rank'] - f500['rank']

print(rank_change)

rank_change =  f500["previous_rank"] - f500["rank"]

rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

#describe()
rank = f500['rank']
rank_desc = rank.describe()


prev_rank = f500['previous_rank']
prev_rank_desc= prev_rank.describe()

#Method Chaining
zero_previous_rank = f500["previous_rank"].value_counts().loc[0]
# Dataframe Exploration Methods
max_f500 = f500.max(numeric_only=True)
f500_desc = f500.describe()
# Assignment with pandas
f500.loc['Dow Chemical','ceo'] = 'Jim Fitterling'

#Using Boolean Indexing with pandas Objects
motor_bool = f500['industry'] == 'Motor Vehicles and Parts'
motor_countries = f500.loc[motor_bool,'country']



prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()


#mask_zero_prev_rank = f500["previous_rank"] == 0 
#f500.loc[mask_zero_prev_rank, "previous_rank"] = np.nan 
#value_counts_prev_rank = f500["previous_rank"].value_counts(dropna=False) 
#prev_rank_after = value_counts_prev_rank.head()
#Creating New Columns
f500['rank_change'] = f500['previous_rank'] -  f500['rank']
rank_change_desc = f500['rank_change'].describe()




#Challenge: Top Performers by Country
ind_bool_usa = f500['country'] == 'USA'
industry_usa = f500.loc[ind_bool_usa,'industry'].value_counts().head(2)

sector_bool_china = f500['country'] == 'China'
sector_china = f500.loc[sector_bool_china,'sector'].value_counts().head(3)








