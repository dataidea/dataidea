# A comparison operator compares its operands and returns
# a Boolean value based on whether the comparison is 
# True of False

# Table of Contents
# Name              Operation
# Equality          ==
# Inequality        !=
# Greater than      >
# Less than         <
# Greater or equal  >=
# Less or equal     <=

# Examples
# Equality 
check_voila = ('Voila' == 'Viola')

# Inequality 
check_voila = ('Voila' != 'Viola')

# Greater or Equal
greater_or_equal = 34 >= 43

# Tip
print('Voila' == 'Viola' == 'Voila')
#       False == True => False


weight = int(input("Enter your weight: "))
height = int(input('Enter your height: '))

bmi = weight/(height**2)

if bmi > 28:
    print('You are over weight')
elif bmi > 18:
    print('You are normal weight')
else:
    print('You are under weight')


