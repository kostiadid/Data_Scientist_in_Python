import pandas as pd

housing = pd.read_csv('housing.csv')
housing.info()

sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', hue='Overall Qual', palette='RdYlGn',size='Garage Area',sizes=(1,300),style='Rooms',col='Year') 
#sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', hue='Overall Qual', palette='RdYlGn',size='Rooms', sizes=[200,50])
plt.show()

correlation = 'positive'

#Most houses built in 2000 or later have a living area aboveground between 1,000 and 3,000 square feet and sell for more than 100,000 USD.
#Most of the houses with an overall quality rating of four or less were built in 1999 or earlier, have low garage area and six rooms or less.
