# A set is a container/collection 
# that is unordered and immutable

pets = {'dog', 'cat', 'rabbit'}

mixed = {'dog', 21, True}

# print(type(mixed))

# Accessing
# for pet in pets:
#     print(pet)

# Adding items to a set
pets.add('fish')

# Removing items from a set
pets.remove('cat') # remove
pets.discard('rabbit') #discard
pets.pop() # pop removes the last item from the set

# Getting the length of a set
length = len(pets)

# Check membership
'parrot' in pets

# Combine sets
pets.update(mixed)

# # Another way to create a set
# new_pets = set(('parrot', 'rat', 'python'))
# print(type(new_pets))

names_set = {'Viola', 'Akullu', 'Juma', 'Shafara'}

other_names = {'Danny', 'Philo', 'Drileba', 'Viola'}

names_set.update(other_names)

print(names_set)

# Getting the difference
first_numbers = {1, 2, 3, 4}
second_numbers = {3, 4, 5, 6}

difference = first_numbers - second_numbers
difference2 = first_numbers.difference(second_numbers)