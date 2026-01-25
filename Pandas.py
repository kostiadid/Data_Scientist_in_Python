import pandas as pd
f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None

f500_shape = f500.shape
print(f500_shape)


f500_type = type(f500)

#  titles    on top  and a side 
f500_top_6= f500.head(6)
f500_bottom_8=f500.tail(8)


#info
print(f500.info())
float64_dtype = 3
int64_dtype = 7
object_dtype = 6

#type function
industries = f500['industry']
industries_type = type(industries)

#Selecting Rows from a DataFrame by Label
revenues_years = f500[["revenues","years_on_global_500_list"]]
countries = f500.loc[:,"country"]
ceo_to_sector = f500.loc[:,"ceo":"sector"]
print(countries)

#Selecting Rows from a DataFrame by Label
toyota = f500.loc['Toyota Motor']
drink_companies = f500.loc[['Anheuser-Busch InBev','Coca-Cola','Heineken Holding']]
middle_companies = f500.loc['Tata Motors' : 'Nationwide']
print(toyota)

#Selecting Items from a Series by Label
countries = f500.loc[:,'country']
country_counts = countries.value_counts()
print(country_counts)
top_country = 'USA'

hq_locations = f500.loc[:,'hq_location']
hql_counts = hq_locations.value_counts()
print(hql_counts)


#Selecting Items from a Series by Label
countries = f500["country"]
country_counts = countries.value_counts()

india = country_counts.loc['India']
print(india)

north_america = country_counts.loc[['USA','Canada','Mexico']]
print(north_america)
japan_to_spain =  country_counts.loc['Japan':'Spain']

#Summary Challenge
big_movers= f500.loc[['Aviva','HP','JD.com','BHP Billiton'],['rank','previous_rank']]
bottom_companies = f500.loc['National Grid':'AutoNation',['rank','sector','country']]

revenue_giants = f500.loc[['Apple','Industrial & Commercial Bank of China','China Construction Bank','Agricultural Bank of China'],'revenues':'profit_change']





