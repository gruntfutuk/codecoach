#!/usr/bin/env python

# introduces the json format - json, JavaScript Object Notation, is a standard
# commonly used in many programming languages for representing structured
# data in a human readable format

import json  # loads a stanard Python module to deal with json structures

# define person record in dictionary
person = {}
person["firstName"] = "Stuart"
person["surname"] = "Moore"
person["gender"] = "Male"

# write record to file in json format
f = open('example4.txt', 'a')  # note this appends each time script is run
json.dump(person, f)  # the method converts from Python format to json
f.close()
