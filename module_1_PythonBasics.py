# Importing module which implements pseudo-random number generators for various distribution.
import random


# Function that calculates average from list and return result.
def average(n):
    # It's not possible to divide by zero. Try-except allows catching this exception.
    try:
        # Dividing the sum of the value in the list by the quantity of values in the list.
        # Rounding up to 2 values after the decimal point.
        return round((sum(n) / len(n)), 2)

    except ZeroDivisionError:
        # Printing text of error in case of the exception.
        print("Cannot divide by zero")


# Using random.sample() functions to generate random number list.
# Using a range() object as an argument to choose a sample from a range of integers.
random_list = random.sample(range(1001), 100)

# Creating an empty list for sorting purpose.
sort_list = []

# When random_list is empty, then "while" will stop looping.
while random_list:
    # Finding first number from list (first element has 0 index) and assign this value to variable.
    minimum = random_list[0]
    # Using the "for" loop for iterating over a list and comparing with previous number.
    for x in random_list:
        # If new number less than previous number, then assign a new value to variable.
        if x < minimum:
            minimum = x
    # The "append()" method adds a single item to the existing list.
    sort_list.append(minimum)
    # The "remove()" method takes a single element as an argument and removes it from the list.
    random_list.remove(minimum)

# The "for" loop is used for iterating over a list and checking remainder after dividing number from list by 2.
# If remainder is 0 then it is even number.
even_list = [num for num in sort_list if num % 2 == 0]
# A for loop is used for iterating over a list and checking remainder after dividing number from list by 2.
# If remainder is 1 then it is odd number.
odd_list = [num for num in sort_list if num % 2 == 1]

# Printing results. The str() function converts the number into a string.
print("List of random numbers : " + str(random_list))
print("List of sort numbers : " + str(sort_list))
print("List of even numbers : " + str(even_list))
print("List of odd numbers : " + str(odd_list))
print("Average for even numbers is: " + str(average(even_list)))
print("Average for odd numbers is: " + str(average(odd_list)))
