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




#Assignment Using Boolean Arrays
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

trip_length = taxi_copy[:,8]
trip_bool_length = trip_length < 60
print(trip_bool_length)

print(trip_length)
trip_length[trip_bool_length] = 0 
print(trip_length)



# Assignment Using Boolean Arrays (Continued)
# create a new array filled with `0`
zeros = np.zeros([taxi.shape[0], 1])
# append the array to the taxi data to create a new column
taxi_modified = np.concatenate([taxi, zeros], axis=1)
# inspect the last five columns of the first ten rows
# print(taxi_modified[:10, -5:])


bool_taxi = taxi_modified[:,6] == 2


taxi_modified[bool_taxi ,15] = 1

taxi_modified[taxi_modified[:, 6] == 3, 15] = 1
taxi_modified[taxi_modified[:, 6] == 5, 15] = 1




#Challenge: Which Is the Busiest Airport?

JFK_Airport_bool = taxi[:,5] ==2
LaGuardia_Airport_bool = taxi[:,5] == 3
Newark_Airport_bool = taxi[:,5] == 5

jfk = taxi[JFK_Airport_bool]
laguardia = taxi[LaGuardia_Airport_bool]
newark_count = taxi[Newark_Airport_bool]

jfk_count = len(jfk)
laguardia_count = len(laguardia)
newark_count = len(newark_count)


final_list = [jfk_count,laguardia_count,newark_count]
busiest_airport = 0
for i in final_list:
    if i > busiest_airport:
        busiest_airport = i
        
print(busiest_airport)
    
busiest_airport = 'laguardia'









