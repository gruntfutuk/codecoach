# Homework week 3

import sys   # so I can read command line arguments
import json  # so I can read/write data/files in JSON format

dictFile = 'hw3.json'  # name of file to store dictionary of args
argKeys = ['scriptname', 'firstname', 'lastname',
           'genderid', 'location', 'status', 'misc']  # key names for args

# first, add command line arguments to a new dictionary
args = {}     # create empty dictionary to add command lines args to
for counter, arg in enumerate(sys.argv):
    if counter < len(argKeys):
        args[argKeys[counter]] = arg  # append key value pairs
    else:
        print('Excess arguments ignored.')
        break
arglist = []  # new list to hold dictionary of args

# check if file is empty by trying to read it; there are better ways
f = open(dictFile, 'r')
if f.readline() != '':         # if line isn't null, file is not empty
    f.close()                  # close it so can re-opon at start
    f = open(dictFile, 'r')  # open file again, at start
    arglist = json.load(f)     # read previously saved list of arg dictionaries
f.close()                      # close file so can reopen for overwrite

# append new dictionary of command line args to list (empty or reloaded)
arglist.append(args)           # add new arguments dictionary to list

# write latest version of list of dictionaries to file
f = open(dictFile, 'w')
j = json.dump(arglist, f)      # write (or overwrite previous) dictionary list

# all done
f.close()
