person = {
    'first_name': 'John',
    'last_name': 'Tong'
}

# print(person)
ln = person['last_name']

# Adding elements to a dictionary
person['middle_name'] = 'Peter'
person['age'] = 39

# Changing values in a dictionary
person['age'] = 40

# Removing items from a dictionary
person.pop('middle_name')

# finding the number of elements in a dictionary
len(person) 


employees = {
    'manager': {
        'name': 'Juma Shafara',
        'age': 39,
        'email': 'jumashafara@dataidea.org'
    },
    'programmer': {
        'name': 'Calvin Tong',
        'age': 29,
        'email': 'tongcalvin@dataidea.org'
    }
}

employees['manager']['name']








