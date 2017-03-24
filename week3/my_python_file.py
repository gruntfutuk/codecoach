# example script to print the command line arguments
# should be invoked with the command line:
# python my_python_file.py 45 'John Smith'

import sys    # imports the sys module which has the code we need
x = sys.argv  # assigns to x a tuple of the arguments from the command line
print(x[0])   # should output my_python_file.py
print(x[1])   # should output 45
print(x[2])   # should output John Smith
