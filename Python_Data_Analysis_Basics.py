ages = []
for i in moma:
    date = i[6]
    birth = i[3]
    if isinstance(birth,int):
        age = date - birth
    else: age = 0
    ages.append(age)
final_ages = []
final_age = None
for i in ages:
    if i > 20:
        final_age = i
    if i <=20:
        final_age = "Unknown"
    final_ages.append(final_age)



decades = []
for i in final_ages:
    if i is "Unknown":
        decade = i
    else:  
        decade=str(i)
        decade = decade[:-1]
        decade +="0s"
    decades.append(decade)

decade_frequency = {}

for i in decades:
    if i  not in decade_frequency:
        decade_frequency[i] = 1
    else:
        decade_frequency[i] += 1
