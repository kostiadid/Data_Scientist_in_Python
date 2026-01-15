opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if   genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
