# how to sort a random number in python?

sort_number = 15

chosen_number = int(input('type a number between 1 and 20: '))

"""
if sort_number == chosen_number:
    print('you got it')
else:
    ('you are wrong')
"""

while chosen_number != sort_number:
    print('you are wrong! try ig again')

    #ctrl + c = cancel a bad loop

    chosen_number = int(input('type a number between 1 and 20: '))

    print('congrats! you are right')