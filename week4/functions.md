# Functions
Functions allow you to create a block of code that performs a
specific job or function. For instance you can create a function
to compute a number of values and return the result. The advantage
of this approach is that each time you call the function you can
pass in different values according to the needs of your program at
that particular time.  To define a function you use the def keyword
```
def SumNums (x,y):
result = int(x) + int(y)
return result


print SumNums(5,10)
```
Which should output `15`.

The function above takes 2 arguments which it puts in variables x
and y. It then adds then together and returns the result to the
calling statement using the return keyword.  The defining line of
a function is ended with a colon and all statements below are
indented to show they are part of the function.  You can also give
a function a default value. In this case if the argument is not
given in the calling statement the default value will be given.
```
def SumNums (x,y = 20): result = int(x) + int(y)
return result


print SumNums(5)
```
Which should output `25`.
