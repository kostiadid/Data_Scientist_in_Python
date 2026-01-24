taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
#This demonstrates how to filter a date using Boolean conditions.
pickup_month = taxi[:, 1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month== 2

february = pickup_month[february_bool]


february_rides = february.shape[0]


tip_amount = taxi[:,12]

print(tip_amount)

tip_bool = tip_amount > 20
print(tip_bool)
top_tips = taxi[tip_bool,5:14]
