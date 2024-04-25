def getAge(month, year):
    month_diff = 12 - month
    year_diff = 2023 - year

    return str(year_diff) + ' years ' + str(month_diff) + ' months'  
    
age = getAge(year=2000, month=10) # keyword argument
age2 = getAge(10, 2000) # positional argument

print(age)


