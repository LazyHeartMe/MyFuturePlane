# Day-02: Variables, Data Types, Input/Output, f-strings
# py4e.com: Ch 1-2

#--- Exercises ---
#--- Source: https://www.py4e.com/html3/02-variables

'''
Exercise 4:
    Assume that we execute the following assignment statements:
    width = 17
    height = 12.0
    For each of the following expressions, write the value of the expression and the
    type (of the value of the expression).
    1. width//2
    2. width/2.0
    3. height/3
    4. 1 + 2 * 5
'''

width = 17
height = 12.0

print(f'1. width//2 = {width//2}, Type = {type(width//2)}')     # output: 8, Type = <class 'int'>
print(f'2. width/2.0 = {width/2.0}, Type = {type(width/2.0)}')  # output: 8.5, Type = <class 'float'>
print(f'3. height/3 = {height/3}, Type = {type(height/3)}')     # output: 4.0, Type = <class 'float'>
print(f'4. 1 + 2 * 5 = {1 + 2 * 5}, Type = {type(1 + 2 * 5)}')  # output: 11, Type = <class 'int'>

'''
Exercise 5:
    Write a program which prompts the user for a Celsius temperature,
    convert the temperature to Fahrenheit, and print out the converted temperature.
'''

celsius = float(input('Enter temperature in Celsius: '))
fahrenheit = (celsius * 9/5) + 32   # input: 32
print(f'Temperature in Fahrenheit: {fahrenheit}') # output: 89.6