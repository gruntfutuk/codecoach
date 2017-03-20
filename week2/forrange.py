#!/usr/bin/env python
# week 2 - example 3, range

import sys  # so I can use sys.stdout.write instead of print in python 2 & 3
            # python 2: print number,    python 3: print(number, end="")

numbers = range(100, 10, -2)  # range to print in reverse order
for number in numbers:
    sys.stdout.write("%d\t" % (number))  # print with tabs between numbers

sys.stdout.write("\n")                   # print newline before exit
