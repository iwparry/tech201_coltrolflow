# While Loops

# While loops monitor date rather than 'looping over'

x = 0

# while x < 10:             # condition being monitored
#     print(f'its working! -> {x}')
#     x += 4 # incrementer - important here or else we would run an infinite loop!

# Using break

# while x < 10:
#     print(f'its working! -> {x}')
#     if x == 4:
#         break
#     x += 1
#
# print(x)   # x = 4

# Verify user input

# Asking for someone's age
# This can either be an int (20) or a string ("Twenty")

# age = input("What is your age?")
# print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:      # preventing unrealistic answers - at time of writing oldest person is 117 years old
        user_prompt = False
    else:
        print("Please provide your answer in digits")
print(f"Your age is {age}")