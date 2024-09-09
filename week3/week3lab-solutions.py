# week 3 lab solutions

################
## Exercise 1 ##
################

# Read in a integer between 1 and 10 from the user.
myint = int(input("Enter an integer between 1 and 10: "))

# Using a while loop, calculate that number to the 5th power.
counter = 0
result = 1
while counter < 5:
    result = result * myint
    counter = counter + 1

# Print out the result.
print(result)


################
## Exercise 2 ##
################

# Ask the user to enter an integer.
myint = int(input("Enter an integer: "))

# As long as the user enters an even integer...
while myint % 2 == 0:

    # Tell the user whether the integer is even or odd.
    print("That integer is even")

    # ... keep asking them for a new integer.
    myint = int(input("Enter an integer: "))

# When they finally enter an odd integer, say goodbye and end the program.
print("That integer is odd. Goodbye!")


################
## Exercise 3 ##
################

# Read in a integer between 1 and 10 from the user.
myint = int(input("Enter an integer between 1 and 10: "))

# Using a for loop, calculate that number to the 5th power.
result = 1
for i in range(5):
    result = result * myint

# Print out the result.
print(result)



################
## Exercise 4 ##
################

# Use a for loop to print out all the even numbers between 1 and 20.

# not including 20
for i in range(20):
    if i%2==0:
        print(i)

# including 20
for i in range(21):
    if i%2==0:
        print(i)



################
## Exercise 5 ##
################

# Rewrite Exercise 1 with two functions:

# (1) a power_five() function that takes an integer as an argument,
# uses a for loop or while loop to calculate that integer to the
# fifth power and prints it out.

def power_five(n):
    result = 1
    for i in range(5):
        result = result * n
    print(result)    
    

# (2) a main() function that reads in the user's integer and calls
# power_five() on that integer.

def main():
    myint = int(input("Enter an integer between 1 and 10: "))
    power_five(myint)

main()

