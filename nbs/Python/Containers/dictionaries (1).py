# A dictionary is an unordered and mutable colletion of items

# Creating 
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }

# Accessing 
# person['middle_name']
person.get('middle_name')


# Adding items 
person['middle_name'] = 'Vee'

# Remove items
person.pop('age')

del person['middle_name']

# Number of elements
len(person)

# Check if a member(key) exists
'middle_name' in person

# Looping through a dictionary
# for key in person:
#     print(person[key])

# Nesting dictionaries
employees = {
    'manager': {
        'name': 'Akullu Viola',
        'age': 29
    },
    'programmer': {
        'name': 'Juma Shafara',
        'age': 30
    }
}

# Accessing nested dictionary
programmer = employees['programmer']

print(programmer['name'])

# Using a dictionary constructer
names = ('a1', 'b2', 'c3')
dictionary = dict(names)
print(dictionary)


