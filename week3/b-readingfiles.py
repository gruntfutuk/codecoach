#!/usr/bin/env python
# working with files, opens a reads a text file filled with random text

f = open('example.txt', 'r')  # f is a file handler

# first version printed line by line (note: intermediate lines are just
# are just empty other than newline characters). Lines are long and
# will probably wrap on the screen, but there are still one line in
# the file

# print(f.readline())

# second version uses for loop to print entire file, with
# line numbers, and ignoring blank lines

x = 1  # initialise counter, so can print number of each line
for line in f:
    if line != "\n":  # ignore lines that are empty but for newline character
        print("{} {}".format(x,line))
        x += 1        # increment counter by one for non empty lines
