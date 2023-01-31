# Control Flow Task 3 - Loops and Lists

# Hello loop
for i in range(10):
    print("hello")    # will print to console 10 times

# Name loop
list_names = []
for num in range(5):
    name = input("What's your name please? ")
    list_names.append(name)
list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())     # loops over the elements in list_names and appends the lowercase versions to list_names_lower
print(list_names_lower)

# Even loop
num_range = list(range(14))
for n in num_range:
    if n % 2 == 0:
        print(f"{n} is even")

# Iterating from 0 to 100 and adding up
one_hundred_sum = 0
for x in range(100):
    one_hundred_sum += x
print(one_hundred_sum)
one_hundred_odd = 0
one_hundred_even = 0
for n in range(100):
    if n % 2 != 0:
        one_hundred_odd += n   # adding odd numbers together
    else:
        one_hundred_even += n  # adding even numbers together
print(one_hundred_odd)
print(one_hundred_even)
