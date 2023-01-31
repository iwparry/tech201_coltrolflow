# Control Flow

# Control Flow -> Flow through a particular decision process.

# if statement

age = 15

# if age >= 18:
#     print("You are the correct age to watch this film and can buy a ticket")

# if age < 18:
#     print("I'm afraid you cannot watch this movie, you are not old enough")

# elif and else statements
film_rating = "PG"

if film_rating.lower() == "universal":
    print("All age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance advised")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("12 rated moves may not be suitable for those under 12, supervision is advised")
elif film_rating.lower() == "15":
    print("You must be 15 years old to watch this film in the cinema")
elif film_rating.lower() == "18":
    print("You must be 18 years old to watch this film in the cinema")
else:
    print("Not a correct rating, please use universal, pg, 12, 12a, 15, 18")

# In Python there are no 'switch statements' or 'case statements'