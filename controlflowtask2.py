# Control Flow Task 2 - If Statements
import random

# Program 1
# Prompts user for hours worked and rate of pay and calculate gross pay for the week, noting the business
# pays 1.5 times their rate for hours worked over 40
hours = input("Please enter the amount of hours worked this week ") # expecting int

if hours.isdigit() and int(hours) >= 0 and int(hours) <= 168:
    rate = input("Please enter your hourly rate ")  # can be int or float
    if rate.isnumeric():
        if int(hours) <= 40:
            pay = int(hours) * float(rate)
            print(f"Your gross pay for the week is £{pay}")
        else:
            spay = 40 * float(rate) # standard pay
            otpay = (int(hours) - 40) * float(rate) * 1.5 # overtime pay
            print(f"Your gross pay for the week is £{spay + otpay}")
    else:
        print("The rate you entered doesn't make sense")
else:
    print("We need you to enter digit hours, please note there are 168 hours in a week")

# Program 2
# Prompt user for a number and return whether the number is odd or even
num = input("Please provide a whole number ") # expecting input of data type int

if num.isdigit() and int(num) % 2 == 0:
    print(f"The number {num} is even!")
elif num.isdigit() and int(num) % 2 != 0:
    print(f"The number {num} is odd!")
else:
    print("You haven't entered a valid number")

# Program 3 - Work in progress
# Have a variable that is assigned a number between 1 and 20, allow the user to guess up to 3 times
# informing them if they need to increase or decrease their guess!
my_num = random.randint(1,20)
counter = 0

guess = input("Please guess a number between 1 and 20 ")
if guess.isdigit() and int(guess) > 0 and int(guess) <= 20:
        if int(guess) > my_num:
            counter += 1
            guess = input(f"Too high! You've used {counter} of 3 guesses. Please guess again ")
        elif int(guess) < my_num:
            counter += 1
            guess = input(f"Too low! You've used {counter} of 3 guesses. Please guess again ")
        else:
            print(f"Correct! The number was {my_num}")

else:
        print("We need a whole number between 1 and 20")

if counter == 3:
        print("Game over!")


# Program 4
# FizzBuzz - Write program that prints numbers from 1-100
# But for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz"
# For multiples of both 3 and 5 print "FizzBuzz":
fizzbuzz = list(range(1,101))
#
for i in fizzbuzz:
    if i % 3 == 0 and i % 5 != 0: # i is only a multiple of 3
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0: # i is only a multiple of 5
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0: # i is a multiple of both 3 and 5
        print("FizzBuzz")
    else:     # i is a multiple of neither 3 nor 5
        print(i)


