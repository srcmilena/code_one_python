"""
imagine you want to print "approved", if the student get an average greater or equal to 7, and "repproved", if the average is less than 7
"""

average = float(input('type the student average: '))

if average >= 7:
    print('you are approved')
elif average >= 5: # does not exist else if in py but elif
    print('recuperation')
else:
    print('you are repproved')