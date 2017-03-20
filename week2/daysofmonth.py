#!/usr/bin/env python

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
