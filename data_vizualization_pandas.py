
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
