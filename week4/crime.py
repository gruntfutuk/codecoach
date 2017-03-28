#!/usr/bin/env python
# WEEK 4 class

# example of using JSON to examine public data sets, in this case
# crime statistics published by UK Police.

import json
import urllib2

# set lilter string (set to null string if no filtering required)
match       = "Lane"

# build the data query - could consider making these arguments :-)
queryurl    = 'http://data.police.uk/api/crimes-street/all-crime'
lattitude   = 'lat=52.6636442'
longitude   = 'lng=-2.4438707'
date        = 'date=2017-01'
querystring = queryurl + "?" + lattitude + "&" + longitude + "&" + date

# raise query and convert to dictionary using JSON
response    = urllib2.urlopen(querystring)
crimes      = json.loads(response.read())

# function to print a crime record (optionally matching street name search)
def printcrime(crime, match=""):
    street = crime['location']['street']['name']
    if match != "":
        if match not in street:
            return
    print('{} {}'.format(crime['category'], street))
    print('http://www.google.com/maps/@{},{}'.format(crime['location']['latitude'], crime['location']['longitude']))


# print all crime records in the query response
for crime in crimes:
    printcrime(crime, match)
