# Control Flow Task 4 - While loops

# Average of integers
num_list = []
while len(num_list) <= 10:
    num = input("Please give us a number ")
    if num.isdigit():
        num_list.append(int(num))
    else:
        print("Whole numbers only please")
    if len(num_list) == 10:
        average = sum(num_list) / len(num_list)
        print(f"The average of the 10 numbers you've provided is {average}")
        break

# Series of 10 (up to 300)
x = 0
while x <= 300:
    x += 10
    print(x)
    if x == 300:
        break

# Luke's solution to part 1 (summing 10 user input numbers)
# While loop solution
amount = 0
number = 0

while True:       # core of the program
    amount += 1      # track the amount of numbers the user has inputted
    number += int(input("Number: "))    # will add each user input to the value of number
    if amount == 10:    # break condition to get out the loop
        break
print(f"Average of numbers inputted: {number / amount}")

# For loop solution

total = 0

for i in range(10):    # we want 10 numbers
    total += int(input("Enter a number: "))

print(f"The total of your inputs is {total}")