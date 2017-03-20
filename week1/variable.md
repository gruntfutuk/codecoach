# Variables
Variables Variables are objects that are held in the computer memory
during the operation of a program Variables are created by assigning
a value to a named object.

a=4 the value of 4 is assigned to a variable called a.

The equals sign = is the assignment operator. Whatever is on the
right hand side is evaluated and assigned to the variable named on
the left hand side.

firstName = "Jon" Variables have types. A type describes what type
of data this is and its properties. Common types in Python String
Integer (numbers) Lists Tuples Dictionaries.

Variables can be mutable (can be changed after creation) or immutable
(can never be changed during the lifetime of a program.

## Lists
Lists are variables that hold lists of data usually with some
common connection. They can then be referenced by the position they
were defined to retrieve the data.

Lists are created with []

a = ["Monday","Tuesday","Wednesday","Thursday","Friday"] create a
list called "a" with the list of weekdays Add the weekend days in
a.append("Saturday") a.append("Sunday")

Lists are a mutable variable type

You retrieve the data by asking for the entry in the list by its
position.

a[1] `Tuesday' In python the first position is always referenced
by 0

Tuples Tuples are similar to lists in that they are ordered sequences
of values. However, the key difference is that tuples are immutable
and can't be changed once created. Tuples are created with ()

daysOfWeek =
("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

Even though a Tuple is created with () they are referenced by []

daysOfWeek[2] `Wednesday'

## Dictionaries
Dictionaries are lists of key/pair values Dictionaries
are a mutable structure. Create a dictionary with curly braces {}
and reference with []

Person = {"firstName": "Jon", "lastName": "Farmer"} Person["firstName"]
`Jon'

You can add a new key/value pair to an existing dictionary

Person["age"] = 99

Multi-Level Lists, Tuples.  You can assign other lists, tuples and
dictionaries as entries to a list or tuple.

Create a new list a = []

add the Person dictionary to the list. a.append(Person)

add an integer to the list a.append(2)

add a string to the list

a.append("3")

Refer to the dictionary in position 1 in the list and return the
firstName key. a[0]["firstName"] `Jon'

# Homework

## Homework 1
Create a list to hold the colours of the rainbow.
Experiment with retrieving the colours from the list

## Homework 2
Create 3 dictionaries that hold the forename, surname, age and
occupation of 3 people. Assign these 3 dictionaries each as an entry
to a list and experiment with retrieving the keys of forename,
surname, age and occupation for each position in the list.
