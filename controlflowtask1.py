# Control Flow Task 1 - Improved Movie Rating Program

# This program should:
# Ask user for their age
# Program should tell them what rated movies they can watch (of U, PG, 12, 15, 18)
# Do not let the user enter incorrect values such as 'cheese' or enter unrealistic values like 1000
# Using if, elif, else

age = input("What is your age? ")

if age.isdigit() and int(age) > 0 and int(age) < 117:
    if int(age) >= 18:
        print("You are old enough to buy tickets for any movie")
    elif int(age) < 18 and int(age) >= 15:
        print("You can buy tickets for films rated U, PG, 12 and 15")
    elif int(age) < 15 and int(age) >=12:
        print("You can buy tickets for films rated U, PG, and 12")
    else:
        print("You can buy tickets for any U rated films, we advise adult supervision for PG rated films")
else:
    print("The value you've entered is invalid, please enter a digit value for your age (e.g. 12) and a realistic one!")