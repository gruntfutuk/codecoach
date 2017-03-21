#!/usr/bin/env python
# Home work is to create a dictionary with names of the months
# and the number of days in them, then print this info out
# appending short or long month for months less than or greater
# 30 days.

# first, create dictionary - note that dictionary have an
# arbitary order however they are created (although Python
# 3.6 and up retain the declaration order, best not to
# depend on this as cannot be sure which version script
# might run on)

months = {"January": 31,
          "February": 28,
          "March": 31,
          "April": 30,
          "May": 31,
          "June": 30,
          "July": 31,
          "August": 31,
          "September": 30,
          "October": 31,
          "November": 30,
          "December": 31}

# loop through dictionary, printing month names and number of days
print("\n\nDictionary key value pairs for month and number of days ...")
for month in months:
    days = months[month]
    if days < 30:
        comment = "\tShort month."
    elif days > 30:
        comment = "\tLong month."
    else:
        comment = ""
    statement = "The month of {}\t has {} days." + comment
    print(statement.format(month, months[month]))

# loop through again, using items method
print("\n\nAnd now, another technique ...")
for month, days in months.items():
    if days < 30:
        comment = "\tShort month."
    elif days > 30:
        comment = "\tLong month."
    else:
        comment = ""
    statement = "The month of {}\t has {} days." + comment
    print(statement.format(month, months[month]))

# print out again, in alphabetical order
print("\n\nAnd now, in alphabetical order...")
for month in sorted(months):  # returns data sorted on keys by default
    days = months[month]
    if days < 30:
        comment = "\tShort month."
    elif days > 30:
        comment = "\tLong month."
    else:
        comment = ""
    statement = "The month of {}\t has {} days." + comment
    print(statement.format(month, months[month]))
