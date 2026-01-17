content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197


for i in content_ratings:
    content_ratings[i] = (content_ratings[i] / total_number_of_apps) * 100
    
percentage_17_plus= content_ratings['17+']

percentage_15_allowed = ((total_number_of_apps / total_number_of_apps)* 100) - percentage_17_plus


