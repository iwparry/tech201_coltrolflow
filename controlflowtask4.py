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



