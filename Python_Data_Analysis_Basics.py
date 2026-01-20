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
