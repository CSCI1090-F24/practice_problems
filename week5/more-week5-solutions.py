### Create lists
# 1. Make a list of your four favorite items for dinner, `dinner`.

dinner = ["pizza", "artichokes", "chili", "quiche"]

# 2. Make a list of your four favorite items for breakfast, `breakfast`.

breakfast = ["cereal", "fruit", "English muffins", "scones"]

# 3. Create a new list `meals` that is the concatenation of `breakfast` and `dinner`.
meals = breakfast + dinner

# 4. Append three dessert items to `meals`.

meals.append("ice cream")
meals.append("cake")
meals.append("pie")

# or meals.extend(["ice cream", "cake", "pie"])

print(meals)

# 5. Print out the length of each list.
print(len(dinner))
print(len(breakfast))
print(len(meals))


# 6. Print out the first, third, and last element of  `meals`.
print(meals[0], meals[2], meals[-1])

# 7. Print out the second through fifth elements (inclusive) of `meals`.
print(meals[1:5])

# 8. Print out the first through third elements (inclusive) of `meals`.
print(meals[:3])

# 9. Print out the fifth through last element of `meals`.
print(meals[4:])


### Iterating through lists
# 10. Using the for/each syntax (i.e., `for item in mylist`),
# print out every element in `meals` that contains an `e`.

for food in meals:
    if "e" in food:
        print(food, end=" ")
print()

# 11. Using the for/range syntax, print out every element
# in `meals` that has a `t`.

for i in range(len(meals)):
    if "t" in meals[i]:
        print(meals[i], end=" ")
print()



# 12. Using the for/each syntax, create a new list, `s_foods`
# that contains every element in `meals` that has an `s`.
s_foods = []
for food in meals:
    if "s" in food:
        s_foods.append(food)
print(s_foods)


# 13. Print out the difference in length between `meals` and `s_foods`.
print(len(meals) - len(s_foods))


### Functions for lists and strings.
# 14. Create a list of words from the string
# ``four score and four years ago``
words = "four score and four years ago".split()

# 15. Print out the count of ``four`` in that list.
print(words.count("four"))

# 16. Find the index of first instance of the word ``four``
myindex = words.index("four")
print(myindex)

# 17. Use that index to replace that instance
# of ``four`` with ``eleven``.
words[myindex] = "eleven"

# 18. Join the list back into a string called `bad_gettysburg`
# and print it out.
newstring = " ".join(words)
print(newstring)
