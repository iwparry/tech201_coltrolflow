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