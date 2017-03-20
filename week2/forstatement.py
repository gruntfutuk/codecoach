#!/usr/bin/env python
# week 2 - example 2, for statement

words = ['one', 'two', 'three', 'four']

for word in words:
    print(word)
    print("%s has %d letters" % (word, len(word)))
