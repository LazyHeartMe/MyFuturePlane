# Day-02: Variables,Data types, input/output, f-strings
# py4e.com: Ch 1-2

#--- 1)Variables ---

a = 10
b = 5
c = a + b
print(c)  # Output: 15

x = 12.2
y = 14
x = 100
print(x)  # Output: 100
print(x+y)  # Output: 114.2

name = "John"
Name = "Doe"
print(name)  # Output: John
print(Name)  # Output: Doe

a = b = c = 10
print(a, b, c)  # Output: 10 10 10

Name = 'Hridoy'
Age = 21
print(Name, Age)  # Output: Hridoy 21

#--- Theory ---
"""
 ~ Variables are used to store data in a program.
 ~ A variable is a name that refers to a value.
 ~ In Python, you can create a variable by assigning a value to it using the equals sign (=).
 ~ Allocate a piece of memory to store the value and associate it with the variable name.
 ~ Variable names can contain letters, numbers, and underscores, but they cannot start with a number.
 ~ Variable names are case-sensitive
 ~ To assign a value to a variable, use the assignment operator (=).
 ~ You can assign a value to a variable at the time of declaration or later in the program.
 ~ You can also assign the same value to multiple variables in a single line.
"""

#--- Data types ---
"""
~ Python has several built-in data types, including:
    - Numeric types: int, float, complex
    - Sequence types: list, tuple, range
    - Text type: str
    - Set types: set, frozenset
    - Mapping type: dict
    - Boolean type: bool
    - None type: NoneType
~ You can use the type() function to check the data type of a variable.
~ You can use the isinstance() function to check if a variable is an instance of a specific data type.
~ You can use the int(), float(), str(), and bool() functions to convert between different data types."""