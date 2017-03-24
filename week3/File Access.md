# File Access

You can use Python to read and write files to your hard
drive or portable storage such as a USB drive.

To read a file you
must create what is called a *file handler* that will refer to the
open file.

## Opening a file
You create the File Handler using the open command. For example,

`f = open('~/pyfiles/example.txt',r')`

The first argument in `open()` is the name of the file you want to open, the second
argument is the **mode** in which it is to be opened. This can be one of the
following:

| mode | description |
| --- | --- |
| 'r' | read only |
| 'r+' | read and write |
| 'w' | write |
| 'a' | append |

If you open an existing file with the `'w'` mode it will **overwrite**
the file. Use the `'a'` mode to **append** (add) to an existing file.

## Reading a file
Read the entire: `f.read()`
Read just the next line: `f.readline()`

You can use a for loop to move through the file line by line (this uses the
`in` command to mean 'everything in the object that comes next' and objects are
things like ranges, lists, tuples, dictionaries, and files):

```
for line in f:
    print line
```

## Writing a file
To write or append to a file you create a file handler with the 'w' or 'a' mode:

```
f = open('c:\temp\example2.txt','w')
f.write('This is a line of text')
```

## Closing a file
You need to save and close any file you have opened:
```
f.close()
```
If your programme neglects to close the file(s), the results are unpredictable
but may well include loss of the information written to the file, corruption
of the data in the file, or problems reading the file in the future.

# Reading and Writing more complex data using JSON

To simplify the storage of more complex information than simple text, a Python module
can be used that supports the **Javascript Object Notation (JSON)** format, which is a
common standard used for sharing information on the internet regardless of the
programming languages used.

JSON is a human readable format, and looks similar to Python dictionaries at
first glance, but it different. The built in Python JSON module makes it easy
to convert Python data to and from JSON data and to read and write files using
the JSON format.

In summary:
* You can save objects such as lists, tuples and dictionaries to a file.
* You will need to convert the object to a string format.
* You can use the json module to do this.

For example:
```
import json
f = open('c:\temp\example3.txt','w')
x = {}
x['name'] = 'Mike Jones'
x['age'] = '33'
x[“gender'] = 'Male'
j = json.dump(x,f)  # write x to f after converting to json
f.close()
```

You can convert back a saved dictionary from a file:
```
f = open(“c:\temp\example3.txt”,”r+”)
x = json.load(f)
print x['age']
f.close()
```

*Note: If the file does not contain data in the expected format, or if it has more than one
record, the programme will fail.*
