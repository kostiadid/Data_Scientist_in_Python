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
