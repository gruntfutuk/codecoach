# Command Line Arguments
Command line arguments allow you to specify extra information that
you can pass to your Python programme at run time.
An example of this:
`python my_python_file.py 45 'John Smith'`
This command will run the
my_python_file.py file and pass in two extra arguments of `45` and
`'John Smith'`.
Note that all entries on the command line are considered
to be strings, you do not need to use quotes unless you want any
specific argument to include a space (as spaces are used to distinguish
betweem arguments), so in this example, without the quotes around John Smith,
the third print line would only output John and not John Smith.
```
import sys    # imports the sys module which has the code we need
x = sys.argv  # assigns to x a tuple of the arguments from the command line
print x[0]    # should output: my_python_file.py
print x[1]    # should output: 45
print x[2]    # should output: 'John Smith'
```
The first command line argument will be the name of your Python programme.
