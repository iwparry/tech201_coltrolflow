# Tech 201 Control Flow
A Control Flow in Python is simply a controlled decision-making process set by us for the program to follow
### if statements
One of the most basic and most used of our control flow tools is the 'if statement' written as
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
So how do we expand our control flow to consider other conditions? That's where elif and else statements come in.
### elif and else statements
While we can simply write multiple if statements to cover all of the conditions we wish to consider the elif and else statements give us a way to combine the conditions into one control flow decision-making process as opposed to splitting up our criteria into separate if statements. Below is an expanded example using film ratings!
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


