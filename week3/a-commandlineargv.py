#!/usr/bin/env python

# reading arguments given on the command line when script invoked
# (if invoked with nothing after script name, will generate a failure)
import sys     # import module that provides command line arguments
x = sys.argv   # assign to x a list of the command line arguments
print(x[1])    # print the 2nd argument (first will be name of involved script)
