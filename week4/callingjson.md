# Using JSON to Download Data From The Internet
JSON is a very popular way to transfer data across the Internet.
When you use a mobile app it is very likely that the data it gives
you has been sent over the Internet as a JSON file. For instance,
a weather app might pull the details for your local area from a
server which returns the data as JSON.  In most scenarios the JSON
file will use the same protocol as a web page, that is to say you
will use HTTP(S) to fetch the JSON file.  For example:
`http://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2011-08`
The above example fetches the recorded crime data for the area
defined by latitude 52.629729, longitude 1.131592 and for the month
of August 2011.  You can change the parameters in the URL to indicate
which area and month you are interested in. In python we use the
urllib2 module to provide HTTP functions.
```
import urllib2, json
response = urllib2.urlopen(‘https:// http://data.police.uk/api/crimes-street/all-
crime?lat=52.629729&lng=-1.131592&date=2011-08’) json_data = response.read()
crime_data = json.loads(json_data)
for crime in crime_data:
print crime["category"] + " in " + crime["location"]["street"]["name"]
```
The above example pulls the JSON file from the URL specified and
reads it into a string variable called json_data. We then convert
the json_data to a multi-level dictionary using the loads method
of the json module.  We then use a for loop to list the data we are
interested in for each return recorded crime.

In most circumstances you will need to use an online JSON parser
to see the structure of the JSON data in a human readable format.
The website at `http://jsonviewer.stack.hu/` is ideal for this
purpose.

