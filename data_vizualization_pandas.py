
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


#Grid Charts
plt.figure(figsize=(10, 12))
plt.subplot(3, 2, 1)
plt.subplot(3, 2, 2)
plt.subplot(3, 2, 3)
plt.subplot(3, 2, 4)
plt.subplot(3, 2, 5)
plt.subplot(3, 2, 6)

plt.show()

plt.figure(figsize=(10, 12))
for i,day in zip(range(1,7),days):
    plt.subplot(3, 2, i)
    plt.plot(traffic_per_day[day]['Hour (Coded)'],
        traffic_per_day[day]['Slowness in traffic (%)'])
    plt.title(day)
    plt.ylim([0,25])
  
plt.subplot(3, 2, 6)
for day in days:
    plt.plot(
        traffic_per_day[day]['Hour (Coded)'],
        traffic_per_day[day]['Slowness in traffic (%)'],
        label=day)
    plt.legend()
    plt.ylim([0,25])
plt.show()



#Storytelling Data Visualization

death_toll = pd.read_csv('covid_avg_deaths.csv')
deaths = [2387, 126203, 227178, 295406]
proportions = [round(death/295406, 2) for death in deaths]
xmax_vals = [round(0.5 + proportion * 0.3, 3) for proportion in proportions]

fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(6,8))

for ax in axes:
    ax.plot(death_toll['Month'], death_toll['New_deaths'],
            color='#af0b1e', alpha=0.1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.tick_params(bottom=False, left=False) 
    for location in ['left', 'right', 'top', 'bottom']:
        ax.spines[location].set_visible(False)
        
axes[0].plot(death_toll['Month'][:3], death_toll['New_deaths'][:3],
         color='#af0b1e', linewidth=2.5)
axes[1].plot(death_toll['Month'][2:6], death_toll['New_deaths'][2:6],
         color='#af0b1e', linewidth=2.5)
axes[2].plot(death_toll['Month'][5:10], death_toll['New_deaths'][5:10],
         color='#af0b1e', linewidth=2.5)
axes[3].plot(death_toll['Month'][9:12], death_toll['New_deaths'][9:12],
         color='#af0b1e', linewidth=2.5)

axes[0].text(0.5, -80, '0', alpha=0.5)
axes[0].text(3.5, 2000, '1,844', alpha=0.5)
axes[0].text(11.5, 2400, '2,247', alpha=0.5)

axes[0].text(1.1, -300, 'Jan - Mar', color='#af0b1e',
         weight='bold', rotation=3)
axes[1].text(3.7, 800, 'Mar - Jun', color='#af0b1e', weight='bold')
axes[2].text(7.1, 500, 'Jun - Oct', color='#af0b1e', weight='bold')
axes[3].text(10.5, 600, 'Oct - Dec', color='#af0b1e', weight='bold',
        rotation=45)

axes[0].text(0.5, 3500, 'The virus kills 851 people each day',
         size=14, weight='bold')
axes[0].text(0.5, 3150, 'Average number of daily deaths per month in the US',
         size=12) 

for ax, xmax, death in zip(axes, xmax_vals, deaths):
    ax.axhline(y=1600, xmin=0.5, xmax=0.8,
               linewidth=6, color='#af0b1e',
               alpha=0.1)
    ax.axhline(y=1600, xmin=0.5, xmax=xmax,
               linewidth=6, color='#af0b1e')
    ax.text(7.5, 1850, format(death, ','),color='#af0b1e', weight='bold')
plt.show()




