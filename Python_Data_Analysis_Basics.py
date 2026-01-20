
# Working with the dataset, we'll learn how to do the following:      //'artworks_clean.csv'

# Calculate the artist's age when they created their artwork
# Analyze and interpret the distribution of artist ages
# Create functions that summarize our data
# Print summaries in an easy-to-read-way


from csv import reader

# Read the `artworks_clean.csv` file
with open('artworks_clean.csv') as opened_file:
    read_file = reader(opened_file)
    moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for i in moma:
    date = i[6]
    if date != '':
        date = int(date)
    i[6] = date
    
