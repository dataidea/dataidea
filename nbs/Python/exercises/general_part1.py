# Homework
# Theory 

# Python Overview:
# What are the fundamental components of a Python program, and how does Python execute code?

# Python Variables:
# Explain the differences between mutable and immutable data types in Python and provide 
# examples of each.

# Python Operations:
# Discuss the importance of operator precedence in Python and how it impacts the evaluation
#  of expressions.

# Python Collections:
# Compare and contrast the usage of lists, tuples, sets, and dictionaries in Python, 
# highlighting their key characteristics and when to use each.

# Practical
# Problem: Pizza Party

# You're organizing a pizza party and want to ensure there's enough pizza for everyone
#  attending. Each pizza has 8 slices. Write a Python script that calculates the number 
# of pizzas needed based on the number of guests and slices per person.

# Consider the following inputs:

# Number of guests attending the party.
# Slices each guest should have (assume each guest will have the same number of slices).
# Your script should:

# Prompt the user for the number of guests attending.
# Prompt for the number of slices each guest should have.
# Calculate the total number of slices needed.
# Calculate the total number of pizzas required (round up to the nearest whole pizza).
# For instance, if 10 guests are attending and each should have 3 slices, your program 
# should output the number of pizzas needed to fulfill the requirement.

# Solution
number_of_guests = int(input('Enter number of guests: '))
number_of_slices_for_each = int(input('Enter number of slices for each: '))

total_number_of_slices = number_of_guests * number_of_slices_for_each
total_number_of_pizzas = total_number_of_slices / 8

print('Number of pizzas needed for ' + 
      str(number_of_guests) + ' is ' + 
      str(total_number_of_pizzas))


