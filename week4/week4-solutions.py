

## Tuples

### Exercise 1
# 1. Write a function that takes a list of integers and returns
# its length and the value of the maximum integer.

def len_max(l1):
    return len(l1), max(l1)

# 2. Call this function and save what it returns to two variables `a` and `b`.

# Students have a really hard time with this.
# When you call a function that returns something
# you need to *DO* something with what it returns.
# Here we are saving what it returns to variables.
# one for each item that is returned.
a,b = len_max([5, 7, 2, 24, 3, 9, 12])

# 3. Write a print statement to print out the values of `a` and `b`.
print(a, b)

# 4. Call this function again on the same list of numbers and
# save what it returns to a single variable `c`.

c = len_max([5, 7, 2, 24, 3, 9, 12])

# 5. Write a print statment that uses `c` to print out the same thing
# you printed out in step 3.

print(c[0], c[1])

# 6. Change the value of `a` to `25`.
a = 25

# 7. Now try to change the value of of the first element in `c` to 25.
# What happens? Why? 

# This is how you would do it, but it doesn't work.
# Tuples are immutable. You can't change their values.
# c[0] = 25


### Exercise 2
# and whether or not (`True` or `False`) you like cilantro.

# 1. Create a tuple containing your name, your favorite integer,
# the color of your shirt, your graduation year divided by 3,
mytup = ("Emily" "navy blue", (2023/3), True)

# 2. Loop through the tuple to print out each element on a separate line.
for t in mytup:
    print(t)

# 3. Try to use indexing to add your favorite sports team to the tuple.
# What happens? Why?
# This fails. Tuples are immutable.
# mytup[4] = "Revolution"


## Dictionaries

### Exercise 1
# 1. Create a dictionary that maps five color words to the number of letters in that color word (e.g., `"blue"` would map to `4`, `"yellow"` would map to `6`).
# 2. Loop through the **`keys`** in the dictionary to produce output like this:

# ```
# blue has 4 letters
# yellow has 6 letters
# red has 3 letters
# ```
#etc.

color_chars = {"blue":4, "yellow":6, "red":3, "green":5, "burnt sienna":12}
for k in color_chars:
    print(k, "has", color_chars[k], "letters")


### Exercise 2
# 1. Create two empty dictionaries, `oneway` and `otherway`.
# Read in the file `testfile.txt` line by line, and call
# split on each line to create a list of two elements for each line.
# Add the first element as the key to the `oneway` dictionary,
# with the second element as that key's corresponding value.
# Then add the second element as the key to the `otherway` dictionary,
# with the first element as that key's corresponding value.

# create empty dictionaries 
oneway = {}
otherway = {}

# open the file
f = open("favorite_fruits.txt", encoding="utf-8")

# go through the file line by line
for line in f:

    # split each line on space
    things = line.split()

    # enter them into the dictionaries
    oneway[things[0]] = things[1]
    otherway[things[1]] = things[0]

# close the file
f.close()

# 2. Print out the number of keys in `oneway`
# and the number of keys in `otherway`.
# Why are they not the same?

print("oneway has", len(oneway.keys()), "keys")
print("otherway has", len(otherway.keys()), "keys")

# They are not the same because there were duplicates
# in the fruit list. Some people liked the same fruit.
# Keys in dictionaries are unique!
