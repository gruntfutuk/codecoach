#!/usr/bin/env python

# write a text file of several lines using a loop

f = open('example2.txt', 'a')  # the 'a' is for append, 'w' would overwrite
x = range(1, 10)
for line in x:
    f.write("This is line number {}\n".format(line))
f.close()
