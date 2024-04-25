pets = ['dog', 'cat', 'rabbit', 'monkey']

# A python list is an ordered container

# indexing
# print(pets[2])
# range of indexes
# print(pets[1:3])

# Adding items
pets.append('parrot') #appending

pets.insert(2, 'fish') #inserting


# Delete items
# pop
pets.pop()

# remove
pets.remove('fish')

# del
del pets[1]

# length of a list
len(pets)

# Change a value 
pets[1] = 'python'

# Check if an item exist
'monkey' in pets

# Extend a list
other_pets = ['turtle', 'horse', 'rat']

pets.extend(other_pets)

# Get all items in a list one by one
# for pet in pets:
#     # print(pet)

# Another way to create lists
friends = list(('Vee', 'Shafara'))
print(type(friends))





