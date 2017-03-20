#!/usr/bin/env python
#
# Homework from w/b 06/03/2017
# 2. Create 3 dictionaries
# that hold the forename, surname, age and occupation of 3 people.
# Assign these 3 dictionaries each as an entry to a list and
# experiment with retrieving the keys of forename, surname, age and
# occupation for each position in the list.


print("\n\n")
homework = "HOMEWORK 2 - experiment with dictionaries"
print(homework)
print("-" * len(homework)+"\n")

people = []
people.append({'forename':   'Alice',
               'surname':    'Smith',
               'age':        9,
               'occupation': 'student'})
people.append({'forename':   'Paul',
               'surname':    'Smith',
               'age':        19,
               'occupation': 'mechanic'})
people.append({'forename':   'Helen',
               'surname':    'Jones',
               'age':        32,
               'occupation': 'solicitor'})

print("List first entry:\t", people[0])
print("List second entry:\t", people[1])
print("List third entry:\t", people[2])

forenames = []
forenames.append(people[0]['forename'])
forenames.append(people[1]['forename'])
forenames.append(people[2]['forename'])
print("Forenames:\t\t", forenames)

# lets print out all entries in a table
print("\n")
header = "Forename       Surname        Age   Occupation"
print(header)
print("-" * len(header))
for each in people:
    print("%-15s%-15s%3d   %s" % (
          each["forename"],
          each["surname"],
          each["age"],
          each["occupation"]))
print("\n")
