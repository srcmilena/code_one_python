# converting

# python has dynamic typage and strong

age = '5'
number1 = '3'
number2 = '6'

# print(number1 + number2) # result = 1020 (concatening)

print(age, type(age))
entire_age = int(age)
print(entire_age, type(entire_age))

# int() = to int / example str '20' to int 20
# str() = to string / example int 20 to '20'
# float() = to float / example str '2.0' to float 2.0
# bool() = to boolean

# height = (input('type your height: ')) # equal to string
height = float(input('type your height: ')) # equal to float
# always convert to number or float because the input i python is always a string
print(height, type(height))