# Loops in Python are used to repeatedly execute a block of code.
# The for loop in Python is used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.

for i in range(10):
    print(i)

# The while loop in Python is used to execute a block of code repeatedly as long as a given condition is true.

i = 0 
while i < 5:
    print(i)
    i += 1

# Loop control statements change the execution of the loop from its normal sequence. 
# The break statement is used to terminate the loop prematurely when a certain condition is met.

for i in range(7):
    if i == 4:
        break
    print(i)
   
# The continue statement is used to skip the rest of the code inside the current loop for the current iteration only.

i = 0
while i < 12:
    i += 1
    if i == 7:
        
        continue
    print(i)

# The pass statement is a null operation. Nothing happens when it executes. It is used as a placeholder.

for i in range(4):
    if i == 3:
        pass
    print(i)