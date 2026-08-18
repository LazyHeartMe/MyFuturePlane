# Day-02: Variables,Data types, input/output, f-strings
# py4e.com: Ch 1-2

#--- 5)Input/Output ---

#--- Theory ---
"""
~ Input is the process of receiving data from the user or another source.
~ Output is the process of displaying data to the user or sending data to another destination.
~ In Python, you can use the input() function to get input from the user.
~ The input() function reads a line of text from the user and returns it as a string.
~ You can use the print() function to display output to the user."""

floor = input('Enter your floor number: ')
usf = int(floor) + 1
print(usf)  # Output: floor number + 1

grade = float(input('Enter your grade: '))
print(grade)  # Output: the entered grade



#--- Input/Output with f-strings ---

name = input('Enter your name: ')
age = int(input('Enter your age: '))
varsity = input('Enter your varsity name: ')
print(f'Name: {name}, Age: {age}, Varsity: {varsity}')  # Output: Name: <name>, Age: <age>, Varsity: <varsity>.