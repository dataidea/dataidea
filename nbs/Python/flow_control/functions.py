# # A function in python is a group statements that perform a particular task

# def calculateBodyMassIndex(weight_kg, height_m):

#     body_mass_index = weight_kg / pow(height_m, 2)

#     rounded_bmi = round(body_mass_index, 2)

#     print('The body mass index of a person weighing ' + str(weight_kg) + 
#     'kgs and are ' + str(height_m) + 'metres tall is ' + str(rounded_bmi))




# persons = [
#     {
#         'name': 'tinye',
#         'height': 1.7,
#         'weight': 73
#     }, 
#     {
#         'name': 'juma',
#         'height': 1.6,
#         'weight': 59
#     }
#     , 
#     {
#         'name': 'shafara',
#         'height': 1.5,
#         'weight': 59
#     }
#     ]

# for person in persons:
#     # calculateBodyMassIndex(person['weight'], person['height'])

# def greeter(name):
#     message = 'Hello ' + name
#     print(message)

# greeter('Tinye')

# def addNumbers(number1, number2):
#     sum = number1 + number2
#     print(sum)

# addNumbers(3, 27)
# write a function that divide, multiply, subtract 2 numbers
    
# def greet(name='you'):
#     message = 'Hello ' + name
#     print(message)

# greet()

#  Return Statement

# def addNumbers(number1, number2):
#     sum = number1 + number2
#     return sum
#     print('statement outside the return statement')

# summation = addNumbers(56, 4)

# print(summation)

# lambda functions

calculateBMI = lambda weight_kg, height_m: round((weight_kg/(height_m ** 2)), 2)


print(calculateBMI(67, 1.7))









