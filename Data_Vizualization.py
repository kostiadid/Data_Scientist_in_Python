# Plot and customize a line graph using Matplotlib
# Visualize time series with line graphs
# Interpret line plots by identifying types of change



import pandas as pd
import matplotlib.pyplot as plt

who_time_series = pd.read_csv('WHO_time_series.csv')
who_time_series = pd.DataFrame(who_time_series)
who_time_series['Date_reported'] =pd.to_datetime(who_time_series['Date_reported'])
print(who_time_series.head())

print(pd.DataFrame(who_time_series).info())



argentina = who_time_series[who_time_series['Country']=='Argentina']
plt.plot(argentina['Date_reported'],argentina['Cumulative_cases'])
plt.title('Argentina: Cumulative Reported Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')

plt.show()
argentina_graph_type = 'exponential'



# Italy  / UK/France

france = who_time_series[who_time_series['Country'] == 'France']
uk = who_time_series[who_time_series['Country'] == 'The United Kingdom']
italy = who_time_series[who_time_series['Country'] == 'Italy']

plt.plot(france['Date_reported'],france['Cumulative_cases'],label='France')
plt.plot(uk['Date_reported'],uk['Cumulative_cases'],label='The UK')
plt.plot(italy['Date_reported'],italy['Cumulative_cases'],label='Italy')

plt.legend()
plt.show()

greatest_july = 'The UK'
lowest_july = 'France'
increase_march = 'Italy'


#Scatter Plots and Correlations
bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.plot(bike_sharing['dteday'],bike_sharing['casual'],label='Casual')
plt.plot(bike_sharing['dteday'],bike_sharing['registered'],label='Registered')
plt.title('Bikes Rented: Casual vs. Registered')
plt.xlabel('Date')
plt.ylabel('Bikes Rented')
plt.legend()
plt.xticks(rotation=30)
plt.show()








