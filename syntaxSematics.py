# The syntax of the Python programming language is the set of rules that defines how a Python program will be written and interpreted (by both the runtime system and by human readers).
# Indentation: Python uses indentation to define blocks of code. Each level of indentation is a block, and it starts with a colon (:) and ends when the indentation decreases.
# Python comments are used to explain the code thus Python ignore this comments and it uses '#'.
# Statement are instruction written in the source code for execution.
# Expression only contain identifier, literals, and operators. They are used for evaluation.

# Conditional statements in Python are used to make decisions based on certain conditions.
# The if statement is used to test a specific condition. If the condition is true, the block of code under the if statement will execute.  

x = 5
if x > 5:
    print("x is greater than 5")

# The else statement is used to execute a block of code if the condition in the if statement is false.

x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")    

# The elif statement, short for else if, is used to check multiple conditions.
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")    