# Homework week 3

import sys   # so I can read command line arguments
import json  # so I can read/write data/files in JSON format

# first, add command line arguments to a new dictionary
args = {}
counter = 0
for arg in sys.argv:
    args[counter] = arg  # append key value pair using arg position as key
    counter += 1

# check if file is empty by trying to read it; there are better ways
f = open('hw3.json', 'r')
emptyfile = f.readline() == ''
f.close()

# if the file is empty, create list, add dictionary
if emptyfile:
    arglist = [args]

# if the file is not empty, retrieve data and add new dictionary
else:
    f = open('hw3.json', 'r')
    arglist = json.load(f)  # read previously saved list of arg dictionaries
    arglist.append(args)    # add new arguments dictionary to list
    f.close()               # close file so can reopen for overwrite

# write latest version of list of dictionaries to file
f = open('hw3.json', 'w')
j = json.dump(arglist, f)  # write (or overwrite previous) dictionary list
f.close()
