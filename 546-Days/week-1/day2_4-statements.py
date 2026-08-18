# Day-02: Variables,Data types, input/output, f-strings
# py4e.com: Ch 1-2

#--- 4) Statements ---

#--- Theory ---
"""
 ~ A statement is a complete instruction that performs an action in a program.
 ~ Statements can include expressions, assignments, control flow statements, and more.
 ~ In Python, statements are typically written on separate lines, and the end of a statement is indicated by a newline character.
 ~ Some statements can span multiple lines using line continuation characters or parentheses.
 ~ Python supports various types of statements, including assignment statements, conditional statements, loop statements, function definitions, and more.
 ~ Statements are executed sequentially in the order they appear in the program unless control flow statements alter the execution order.
"""

#--- Assignment - storing a value in a variable
name = "Alice"
age = 25

#--- Print - displaying output
print("Hello, World!")

#--- Arithmetic - doing math
total = 10 + 5
result = 20 - 3

#--- Comparison - checking if something is true
is_adult = age >= 18

#--- Conditional - doing something if true
if age > 18:
    print("You are an adult")

#--- Loop - repeating something
for i in range(3):
    print(i)

#--- Function - reusable code block
def greet(person):
    return f"Hi, {person}!"

#--- Method call - using built-in functions
text = "hello".upper()


# This all demonstrates different types of statements in Python, which are the building blocks of a program.