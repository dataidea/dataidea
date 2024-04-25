def calculateBMI(height, weight):
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 3)
    return rounded_bmi

# body_mass_index = calculateBMI(1.7, 80)

# if body_mass_index > 24:
#     print("You are overweight")
# elif body_mass_index > 18:
#     print("You are normal")
# else:
#     print("You're underweight")


# entered_mark = int(input('Enter your mark: '))

# pass_mark = 50

# if entered_mark > 79:
#     print('Grade A')
# elif entered_mark > 69:
#     print('Grade B')
# elif entered_mark > 59:
#     print('Grade C')
# elif entered_mark > 49:
#     print('Grade D')
# else:
#     print('You never made it')



# response = input(' Are you 18+ ? \n Enter n for no or y for yes: ')

# if response == 'n':
#     print("You're not allowed")
# elif response == 'y':
#     interest = input(' Are you interesed in men or women? \n Enter m for men or w for women: ')
#     if interest == 'm':
#         print('Display men pictures')
#     elif interest == 'w':
#         print('Display women pictures')




bmi = calculateBMI(1.7, 67)

print(bmi)

print('Normal') if 18 <= bmi <= 24 else print('Not normal')

# statement1 if condition else statement2

