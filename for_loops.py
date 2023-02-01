# Looping

# For loop

# Define an iterator number and cycle through a collection of data (lists or dictionaries)
# for each entry in the data structure.

# Creating a for loop

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name":"Bronson", "money":"$0.05"}, 2:{"name":"Masha", "money":"$3.66"}, 3:{"name":"Roscoe", "money":"$1.14"}}

# for num in list_data:
#     print(num * 2)

# Nested for loop
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# Loops for dictionaries

# for item in dict_data.values():
#     print(item)
#
# for item in dict_data.values():
#     for embed_value in item.values():   # nested loop
#         print(embed_value)
#
# for items in dict_data.values():
#     print(items["money"]) # returns just the values corresponding to "money" keys

# Loops and if statements

list1 = [1, 2, 3, 4, 5]
for num in list1:
    if num == 3:
        print("I found three!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")

one_hundred = list(range(1, 100))
for i in one_hundred:
    if i % 2 == 0:
        print(i)