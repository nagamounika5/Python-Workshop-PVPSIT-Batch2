def evenOdd(number):
    if number%2 == 0:
        print('Even Number')
    else:
        print('Odd Number')
        

def leap_year(year):
    if year%400 == 0:
        print('Lear year')
    elif year%4 == 0 and year%100 != 0:
        print('Leap year')
    else:
        print('Not Leap year')