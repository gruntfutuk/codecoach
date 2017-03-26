#!/usr/bin/python
# Homework week 3

# store command line arguments in a dictionary, in a list, in a file
# append to list on file on subsequent runs
# (only ever one stored list, but will contain dictionary for every run)

import sys   # for command line arguments
import json  # so can read/write data/files in JSON format
import os    # to check for file existing using op system

dictFile = 'hw3alt.json'  # name of file to store dictionary of args
argKeys = ['scriptname', 'firstname', 'lastname',
           'genderid', 'location', 'status', 'misc']  # key names for args


# function to do the bulk of the work of the programme
def addArgs(f):
    # first, add command line arguments to a new dictionary
    args = dict(zip(argKeys, sys.argv))  # add with matching keys by position
    # add any excess arguments as a list
    if len(sys.argv) > len(argKeys):
        args['unusedargs'] = sys.argv[len(argKeys):]

    # retrieve any stored dictionary list of command line arguments
    if os.stat(dictFile).st_size > 0:
        arglist = json.load(f)
    else:
        arglist = []

    # append new dictionary of command line args to list (empty or reloaded)
    arglist.append(args)        # add new arguments dictionary to list

    # write latest version of list of dictionaries to file
    f.seek(0)
    json.dump(arglist, f)       # write (or overwrite previous) dictionary list
    f.truncate()


# if dictionary file exists (empty or not) add args, otherwise complain
def main():
    try:
        with open(dictFile, 'r+') as f:  # open file for read/write
            addArgs(f)                   # add the cl args to dict list file
    except IOError as e:                 # throw error if no file or can't write
        print('Trouble opening file {}.'.format(dictFile))
        return e


if __name__ == '__main__':
    main()
