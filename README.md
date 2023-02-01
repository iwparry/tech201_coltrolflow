# Tech 201 Control Flow
A Control Flow in Python is simply a controlled decision-making process set by us for the program to follow
### if statements
One of the most basic and most used of our control flow tools is the '`if` statement' written as
```
if "condition to be met is met (is True)":
   "code to be executed" 
```
Here we tell Python to look at a condition, or a statement, and evaluate whether or not its true. If the condition is met, then Python will execute the code in the indentation. Note that the indentation is requirement or Python will give us an `IndentationError`. Let's look at an actual example say evaluating whether an induvidual is of suitable age to watch a movie
```
age = 19
if age >= 18:
   print("You are the correct age to watch this film and can buy a ticket")
```
In this example Python will print the string within our print statement to our console because the `age` variable satisfies our set criteria in this example.

In the example above there really isn't much going on because we have one simple line of code to be executed. We also should think about what happens if the condition we've currently set is not met. In this case it does nothing because we haven't given Python any instructions on what to do if our condition is not met.
So how do we expand our control flow to consider other conditions? That's where `elif` and `else` statements come in.
### elif and else statements
While we can simply write multiple `if` statements to cover all the conditions we wish to consider the `elif` and `else` statements give us a way to combine the conditions into one control flow decision-making process as opposed to splitting up our criteria into separate `if` statements. Below is an expanded example using film ratings!
```
film_rating = "universal"

if film_rating == "universal":
    print("All age groups can watch this film")
elif film_rating == "pg":
    print("General viewing but parental guidance advised")
elif film_rating == "12" or film_rating == "12a":
    print("12 rated moves may not be suitable for those under 12, supervision is advised")
elif film_rating == "15":
    print("You must be 15 years old to watch this film in the cinema")
elif film_rating == "18":
    print("You must be 18 years old to watch this film in the cinema")
else:
    print("Not a correct rating, please use universal, pg, 12, 12a, 15, 18")
```
In our code block above we have an `if` statement followed by a series of `elif` statements, and an `else` statement at the end. `elif` statements are written similarly to `if` statements with a condition and code to execute in the case that the condition is met. 

So what do they actually do? `elif` allows us to introduce other conditions to our control flow and an instruction to be executed should our `if` statement's condition isn't met, and as we can see we can add as many `elif`'s as we want, it's up to us how specific we want our control flow to be. Of course looking at the above example we know there are only a few film ratings, however we could assign absolutely anything to our `film_rating` variable, and we know we don't have the time to write an `elif` statement for every possible value! So after we know we've covered the conditions we care about, i.e. every valid film rating in our example, we can end our control flow process with an `else` statement, this simply executes an instruction in the circumstance that none of the previous conditions of the control flow have been met. 

Here's a simple example showing `if`, `elif`, and `else` being utilised.
```
my_age = 25

if age == 25:
    print("Yes! I'm 25 years old")
elif age > 25:
    print("No! I'm younger than that")
else:
    print("Thanks, but I'm older")
```
## Loops
### for loops
Another powerful tool we can use in our control flow is a loop, and in Python we have two types of loop, the first and the most commonly used of these loops is the `for` loop.

What we do with `for` loops is we define an iterator variable and cycle through a collection of data (lists, dictionaries, even strings) for each entry in the data structure.

Here is how we create a `for` loop
```
my_list = [a, b, c]

for i in my_list:
   # code to execute for each element i in my_list
```
As previously mentioned we use `for` loops to cycle through a collection of data (we've used a list in the example above). When creating theses we always use the keywords `for`, obviously indicating that we are making that particular loop, and `in` this keyword is used to link our iterator to our target list. Note that above we set our iterator to `i`, there are no constraints on what we can set our placeholder variable to we can set it like any other variable, however these are conventionally single letters or a word that makes sense (e.g. working with a list call 'dogs', 'dog' would be a suitable placeholder).Note this variable only exists inside the loop as an iterator.

A more concrete example of a `for` loop
```
list_data = [1, 2, 3, 4, 5]

for num in list_data:
     print(num * 2)    # this code will be executed for each element in list_data
```
The above will print every number from `list_data` times 2 to our console. Of course, it is very useful to have a tool like this to cycle through this data, especially when these collections are larger! However, there may be instances where we do not wish for our code to be executed for every single element in a collection of data. Suppose we wanted to create a list of numbers from 1 to 100 (not including), but we only wanted even numbers? How do we let Python know to skip odd numbers? We nest `if` statements into our loop!
```
even_list = []       # initialize our even numbers list
for n in range(1, 100):
    if n % 2 == 0: 
       even_list.append(n)
```
In the example above our iterator is `n`, as you can see we have nested an `if` statement in our loop to evaluate each element within our targeted collection of data, in this case every number from 1 to 99. And of course in this case if the element under evaluation meets the set criteria Python will execute the code indented into the `if` statement.

Speaking of nesting, we are also able to nest `for` loops within loops we've created. This is especially useful when dealing with embedded lists and dictionaries (lists/dictionaries that contain more lists/dictionaries). Take below for example.
```
dict_data = {1: {"name":"Bronson", "money":"$0.05"}, 2:{"name":"Masha", "money":"$3.66"}, 3:{"name":"Roscoe", "money":"$1.14"}}

for item in dict_data.values():
    for embed_value in item.values():   # nested loop
        print(embed_value)
```
As you can see, `dict_data` is a dictionary where the values are dictionaries themselves. Suppose we simply wanted to print each value from the embedded dictionaries to our console i.e. `Bronson`, `$0.05` etc. We create a nested loop, where in our first loop we are telling Python to cycle over the values of `dict_data`, the embedded dictionaries, and in our nested loop, we are telling Python to cycle through the values contained in each embedded dictionary and print them to our console.