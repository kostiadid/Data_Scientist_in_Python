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



#Assigning Values in Ndarrays 
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

print(taxi_copy[1066,5])
taxi_copy[1066,5] = 1
print(taxi_copy[1066,5])

print(taxi_copy[:,0])
taxi_copy[:,0] = 16
print(taxi_copy[:,0])

print(taxi_copy[550:552,7])
taxi_copy[550:552,7] = np.mean(taxi_copy[:,7])

print(taxi_copy[550:552,7]) 

rows_550_551 = taxi_copy[550:552,:]
