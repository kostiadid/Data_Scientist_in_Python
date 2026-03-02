import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'])
for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
ax.tick_params(bottom=False, left=False)
plt.show()


