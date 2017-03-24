#!/usr/bin/env python
# working with files, opens a reads a text file filled with random text

f = open('example.txt', 'r')  # f is a file handler

# to print entire file, could simply say
# print(f.read())
# or print in a for loop each line using
# print(f.readline())

# print entire file, with line numbers
# ignoring blank lines
x = 1  # initialise counter, so can print number of each line
for line in f:
    if line != "\n":  # ignore lines that are empty but for newline character
        print("{} {}".format(x,line))
        x += 1        # increment counter by one for non empty lines
