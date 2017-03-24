# Homework week 3

import sys   # so I can read command line arguments
import json  # so I can read/write data/files in JSON format

# first, add command line arguments to a new dictionary
args = {}     # create empty dictionary to add command lines args to
counter = 0   # initialise counter, so we can reference key value pairs
for arg in sys.argv:
    args[counter] = arg  # append key value pair using arg position as key
    counter += 1

arglist = []  # new list to hold dictionary of args

# check if file is empty by trying to read it; there are better ways
f = open('hw3.json', 'r')
if f.readline() != '':         # will be True if file is empty
    f.close()                  # close it so can re-opon at start
    f = open('hw3.json', 'r')  # open file again, at start
    arglist = json.load(f)     # read previously saved list of arg dictionaries
f.close()                      # close file so can reopen for overwrite

# append new dictionary of command line args to list (empty or reloaded)
arglist.append(args)           # add new arguments dictionary to list

# write latest version of list of dictionaries to file
f = open('hw3.json', 'w')
j = json.dump(arglist, f)      # write (or overwrite previous) dictionary list

# all done
f.close()
