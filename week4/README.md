# Week 4 Practice Problems

You'll need to know about functions returning stuff for exercise 1. We'll learn that on Thursday. You can just print stuff out for Exercise 1 for now. 

## Tuples

### Exercise 1
1. Write a function that takes a list of integers and returns its length and the value of the maximum integer.
2. Call this function and save what it returns to two variables `a` and `b`.
3. Write a print statement to print out the values of `a` and `b`.
4. Call this function again on the same list of numbers and save what it returns to a single variable `c`.
5. Write a print statment that uses `c` to print out the same thing you printed out in step 3.
6. Change the value of `a` to `25`.
7. Now try to change the value of of the first element in `c` to 25. What happens? Why? 

### Exercise 2
1. Create a tuple containing your name, your favorite integer, the color of your shirt, your graduation year divided by 3, and whether or not (`True` or `False`) you like cilantro.
2. Loop through the tuple to print out each element on a separate line.
3. Try to use indexing to add your favorite sports team to the tuple. What happens? Why?
4. How would you add something to a tuple? (Answer: reassignment or create a tuple by concatenating prior tuple wkth the things you wanted to add as a tuple.)

## Dictionaries

### Exercise 1
1. Create a dictionary that maps five color words to the number of characters in that color word (e.g., `"blue"` would map to `4`, `"yellow"` would map to `6`).
2. Loop through the **`keys`** in the dictionary to produce output like this:

```
blue has 4 characters
yellow has 6 characters
red has 3 characters
```

etc.


### Exercise 2
1. Create two empty dictionaries, `oneway` and `otherway`. Read in the file `favorite_fruits.txt` line by line, and call `split()` on each line to create a list of two elements for each line. Add the first element as the key to the `oneway` dictionary, with the second element as that key's corresponding value. Then add the second element as the key to the `otherway` dictionary, with the first element as that key's corresponding value.
2. Print out the number of keys in `oneway` and the number of keys in `otherway`. Why are they not the same?
 

