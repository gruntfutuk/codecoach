# WEEK 4 class

Concentrated on functions and loading public data using JSON.

The script `calc.py` calls a simple function to do basic arithmetic, clearly
this is not useful as the capability is built in to Python anyway, however it
does illustrate how functions work, and clearly much more complex (and non
standard) operations could be developed to service a particular need.

I wrote a second version, `calc2.py`, that passed a function rather than a
string with an operator in it. I wrote a set of functions to cover the standard
arithmetic. There is a module already built in to Python that offers this
already for all of the arithmetical and logical operators.

The script `crime.py` loads UK Police crime data (public repository) for a
particular area, coverts that to a Dictionary using the JSON module, and prints
selected data out.

## Homework
Added an app called `weather.py` and `setup.py` (the latter for packaging)
that uses the `Open Weather Map` data source to print a report on the
weather or a named city. (Whilst it fulfils the homework objective, it uses
techniques not covered in the classes and might be too advanced for some
people. It also does not written elegantly.)

### Command Line
It uses command line arguments, and the `click` module to handle the arguments,
to provide lots of options and help text.

### JSON & API
It uses the `requests` module to get the data from Open Weather Map. Note
that an API key is required, which is free but requires registration. The
requests module returns a JSON structure (which is the default response
anyway from Open Weather Map).
