# Day-02: Variables,Data types, input/output, f-strings
# py4e.com: Ch 1-2

#--- 2)Expressions ---

#--- Theory ---
"""
 ~ An expression is a combination of values, variables, operators, and function calls that can be evaluated to produce a result.
 ~ Expressions can be as simple as a single value or variable, or they can be more complex, involving multiple operations and function calls.
 ~ The result of an expression can be assigned to a variable or used directly in other expressions or statements.
 ~ Python supports various types of expressions, including arithmetic expressions, comparison expressions, logical expressions, and more.
 ~ Expressions are evaluated according to the rules of operator precedence and associativity.
"""

x = 10  # 'x' is assigned the value 10
y = 5   # 'y' is assigned the value 5
z = x + y  # 'z' is assigned the result of adding x and y
print(z)  # Output: 15

x = 0.6
x = 10.6*x*(1-x)    # x = 0.6 is used in the calculation: 10.6*0.6*(1-0.6) = 10.6*0.6*0.4 = 2.544
print(x)  # Output: 2.544


#--- Operators ---
"""
 ~ Operators are special symbols in Python that perform operations on values and variables.
 ~ Python supports various types of operators, including arithmetic operators, comparison operators, logical operators, and more.
 ~ Arithmetic operators include +, -, *, /, //, %, and **.
 ~ Comparison operators include ==, !=, <, >, <=, and >=.
 ~ Logical operators include and, or, and not.

 ! Operator sequence:
    ~ Parentheses ()
    ~ Exponentiation (**)
    ~ Multiplication (*), Division (/), Floor Division (//), Modulus (%)
    ~ Addition (+), Subtraction (-)
    ~ Left to right associativity for operators of the same precedence level.
"""

x = 1 + 2**3 / 4 * 5
print(x)  # Output: 11.0

# x = 1 + 8 / 4 * 5
# x = 1 + 2 * 5
# x = 1 + 10
# x = 11.0