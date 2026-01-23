taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')



pickup_month = taxi[:, 1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month== 2

february = pickup_month[february_bool]


february_rides = february.shape[0]
