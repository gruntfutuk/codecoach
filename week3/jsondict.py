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
if f.readline() == '':
    emptyfile = True
else:
    emptyfile = False
f.close()  # could reset but this is all we know for now

# if the file is empty, create list, add dictionary, save to file
if emptyfile:
    arglist = [args]
    f = open('hw3.json', 'w')
    j = json.dump(arglist, f)
    f.close()

# if the file is not empty, retrieve data and add new dictionary
if not emptyfile:
    f = open('hw3.json', 'r')
    arglist = json.load(f)  # read previously saved list of arg dictionaries
    arglist.append(args)    # add new arguments dictionary to list
    f.close()               # close file so can reopen for overwrite

    f = open('hw3.json', 'w')
    j = json.dump(arglist, f)  # overwrite previous list of dictionaries
    f.close()
