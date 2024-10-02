# Week 5 Practice Problems

### Functions that return a value

1a. Write a function that takes three integer arguments and PRINTS OUT the smallest value.

1b. Write a function that takes three integer arguments and RETURNS the smallest value. Have your `main()` function call this function three times, each time saving the return value to a variable. Then print out all three values in one print statement.

1c. Do the same as 1b, but in `main(`) don't save the return values out to variables. Instead, provide the function calls as arguments in `print()`.

2. Write a function that take two strings and returns a string containing the common characters in those two strings. In the `main()` function, print out the return value in two different ways.

### Functions with multiple return statements

3. Write a function that takes two string arguments. Return `True` if the first string comes before the first in the alphabet. Otherwise return `False`. In the `main(`) function, use this function to print out which string is earlier in the alphabet than the other.

4. Write a function that takes an integer argument, `n`. Using a for loop starting at `i=10` and going all the way down 1, check to see if `i` is a divisor of `n`. If it is, immediately return i. If you get all the way through the for loop, then return 1. In the `main()` function, use this function to print out a message like "The largest divisor of your number that is less than 10 is..." whatever gets returned by the function.

### Functions that return multiple values

5. Write a function that returns the min, max, and average of three integer arguments. In the `main()` function print out these values.

6. Write a function that takes two string arguments and returns a string containing all the vowels shared in both strings and its length. Print them both out in `main()`.


### Using Python modules
7. Using `random()`, write a function that generates random integers between 1 and 100 until you get one divisible 7. Return the number you get, and in the `main()` function, print out that number.

8. Using `math()`, experiment with `.floor(), .factorial(), log(), sqrt()`.


## Lists

### Creating lists
1. Make a list of your four favorite items for dinner, `dinner`.
2. Make a list of your four favorite items for breakfast, `breakfast`.
3. Create a new list `meals` that is the concatenation of `breakfast` and `dinner`.
4. Append three dessert items to `meals`.
5. Print out the length of each list.
6. Print out the first, third, and last element of  `meals`.
7. Print out the second through fifth elements (inclusive) of `meals`.
8. Print out the first through third elements (inclusive) of `meals`.
9. Print out the fifth through last element of `meals`.

### Iterating through lists
10. Using the for/each syntax (i.e., `for e in mylist`), print out every element in `meals` that contains an `e`.
11. Using the for/range syntax, print out every element in `meals` that has a `t`.
12. Using the for/each syntax, create a new list, `s_foods` that contains every element in `meals` that has an `s`.
13. Print out the difference in length between `meals` and `s_foods`.

### Functions for lists and strings.
14. Create a list of words from the string ``four score and four years ago``
15. Print out the count of ``four`` in that list.
16. Find the index first instance of the word ``four``
17. Use that index to replace that instance of ``four`` with ``eleven``.
18. Join the list back into a string called `bad_gettysburg` and print it out.


