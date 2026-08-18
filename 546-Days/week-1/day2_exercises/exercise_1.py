# Day-02: Variables, Data Types, Input/Output, f-strings
# py4e.com: Ch 1-2

#--- Exercise ---
#--- Source: https://www.py4e.com/html3/02-variables

# 2.2 Write a program that uses input to prompt a user for their name and then welcomes them.

name = input('What is your name? ')
print(f'Welcome, {name}!')

# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).

hours = float(input('Enter Hours: '))
rate = float(input('Enter rate per hour: '))
pay = hours * rate
print(f'Pay: {pay}')