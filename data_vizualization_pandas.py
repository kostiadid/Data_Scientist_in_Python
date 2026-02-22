
import pandas as pd
import matplotlib.pyplot as plot

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

plot.hist(traffic['Slowness in traffic (%)'])
plot.show()

# we can do it this way    it's might be easer  
traffic['Slowness in traffic (%)'].plot.hist()
plt.title('Distribution of Slowness in traffic (%)')
plt.xlabel('Slowness in traffic (%)')
plt.show()


incidents = traffic.drop(['Hour (Coded)', 'Slowness in traffic (%)'],
                        axis=1)
incidents.sum().plot.bar()
plt.show()


traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Lack of electricity')
plt.show()
traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Point of flooding')
plt.show()
traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Semaphore off')
plt.show()


#Traffic Slowness Over 20%
slowness_20_or_more = traffic[traffic['Slowness in traffic (%)'] >= 20]
slowness_20_or_more = slowness_20_or_more.drop(['Hour (Coded)', 'Slowness in traffic (%)'],axis=1)
incident_frequencies = slowness_20_or_more.sum()
incident_frequencies.plot(kind='barh')
plt.show()





#How Traffic Slowness Change   
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic
    
for day in days:
    traffic_per_day[day].plot.line(x='Hour (Coded)',
                                    y='Slowness in traffic (%)')
    plt.title(day)
    plt.ylim([0,25])
    plt.show()


#all  lines in one  plot 
for day in days:
    plt.plot(
        traffic_per_day[day]['Hour (Coded)'],
        traffic_per_day[day]['Slowness in traffic (%)'],
        label=day)
    plt.legend()
plt.show()

