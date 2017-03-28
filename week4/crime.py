import json, urllib2

response = urllib2.urlopen('http://data.police.uk/api/crimes-street/all-crime?lat=52.651725&lng=-2.485432&date=2017-01')

crimes = json.loads(response.read())


def printcrime(crime):
    print('{} {}'.format(crime['category'], crime['location']['street']['name']))
    print('http://www.google.com/maps/@{},{}'.format(crime['location']['latitude'], crime['location']['longitude']))


for crime in crimes:
    printcrime(crime)
