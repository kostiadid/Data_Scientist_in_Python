



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

#Using iloc to Select by Integer Location
fifth_row=f500.iloc[5]
company_value = f500.iloc[0,0] 

first_three_rows = f500[:3]
first_seventh_row_slice = f500.iloc[[0,6],:5]

#Using pandas Methods to Create Boolean Masks
prev_rank_null = f500["previous_rank"].isnull()
null_prev_rank = f500[prev_rank_null][['company','rank','previous_rank']]

#Working with Integer Labels
prev_rank_is_null = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank= prev_rank_is_null.iloc[:5]

# Pandas Index Alignment
profited_bool = f500['profits'].notnull()
profited = f500.loc[profited_bool]

costs = profited['revenues'] - profited['profits']
f500['costs'] = costs

#Using Boolean Operators
large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500.loc[combined]

filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]

# for me !=  easer  
filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()

#Sorting Values
selected_rows = f500[f500["country"] == "Japan"]
sorted_rows = selected_rows.sort_values('profits',ascending = False)

i = sorted_rows.loc[:,['company','profits']]

top_japanese_company = i.iloc[0] 




