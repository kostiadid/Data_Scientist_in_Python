import pandas as pd
import matplotlib.pyplot as plt

happiness2015 = pd.read_csv("World_Happiness_2015.csv")

first_5 = happiness2015.head(5)
# first_5.info()

mean_happiness = {}
unique_regions = happiness2015['Region'].unique()

for i in unique_regions:
    region_group =  happiness2015[happiness2015['Region']==i]
    mean_happiness[i]= region_group['Happiness Score'].mean()

