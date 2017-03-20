# Basic Control Flow Statements
## Programme flow
The Python interpreter reads script files from top to bottom, one
line at a time, interpreting and executing each line (statement)
in turn (or stopping and reporting an error when it finds something
wrong). This is the standard, linear, flow of execution.

Control flow statements can be used to change the flow to execute
different blocks of code dependent on the outcome of some tested condition,
or to repeat some blocks of codes a certain number of times or until
some tested condition is met.

---

## **if** statements
**if** statements are the most basic of control statements. They
use conditional tests that allow you to specify a statement that
will evaluate to **True** and therefore follow a block of code or
**else**, if not True, follow (optionally) another block of code.
Additional tests for True can be specified using **elif** to mean
else if.

**if**, **elif**, and **else** are always followed by some conditional
expression and ended with a : (colon).

Any non-zero value is treated as True, and a zero value is treated
as False.

```
x = 1
if x:
    print "true"
else:
    print "false"
```
To do equivalence comparisons in **if** statements, you use a double
equals sign as the comparison operator.

```
if x == 1:
    print "x = 1"
elif x == 2:
    print "x = 2"
else:
    print "x is neither 1 or 2"
```
---
## **for** loops
For loops allow you to loop (step) through an object that can be
iterated over such as lists, tuples and dictionaries as well as
strings. You can use the RANGE function to provide an iterable
object containing numbers.

Reference a number based range such as `numbers = range(1,2000,2)`
(i.e. a range from 1 to 2000 iterating by 2 on each pass). Each
loop will assign the next item in the sequence to the variable name
defined immediately after "for" statement from the iterable object
named after the **in**.

```
a = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
for day in a:
    print day
```

You can nest "if" statements and "for" statements to extend the functionality.

```
a = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
for day in a:
    if day == "Monday":
	    print day + ", first day of the working week"
    elif day == "Friday":
	    print day + ", last day of the working week"
    else: print day
```
---
# Conditional expressions
The **if** and **for loop** flow control statements depend on testing some
condition in order to decide what part of a script file should be executed
next.

The test they carry out is known as a *conditional expression*. `x > 20` is an
example of a conditional expression. Whereas numerical expressions, such as
`cost * 1.2` (adding 20% VAT) produce a numerical result, which you can
assign to a variable if you want, e.g. `price = cost * 1.2`, conditional
expressions produce a **boolean** result. That is a result that can have only one
of two values: **True** or **False**. Variables assigned the result of a
conditional expression are boolean variables (rather than integer, float,
string, etc. variables). You can assign a boolean value explicitly, e.g. `likesbeer =
True`, or as the result of a conditional expression, e.g. `likesbeer =
numberofbeers > 3` (assuming numberofbeers has been set to the number of beers
a person has bought for themself).

Conditional expressions are also known as **boolean expressions** or **logical
expressions**.

Increasingly complex conditions can be created, much as in numerical
expressions, using brackets () and logical operators. The operators include:
`<`, `<=`, `>`, `>=`, `==`, `!=`, and, with lower precedence, `and`, `or`, and `not`.
(`!=` means not equal, by the way.)

The table below shows the use of these operators. In each case, either True or False is
returned, there are no other options.

| Expression | Description |
| --- | --- |
| x < y | returns True if x is less than y |
| x <= y | returns True if x is less than or equal to y |
| x > y | returns True if x is greater than y |
| x >= y | returns True if x is greater than or equal to y |
| x ==  y | returns True if x is equal to y |
| x != y | returns True if x is not equal to  y |
| not x | returns True if x is False |
| x and y | returns True only if both x and y are True |
| x or y | returns True if either of x or y are True |

Logical operators can be chained, e.g. `10 <= x <= 20` which means each test
pair is evaluated and the results are *ANDed* together.

---

# Homework

Create a dictionary with the names of the months of the year as
keys and the number of days in the month as the values.

Loop through the dictionary printing each month name and how many
days it contains. On months that contain 28 or 29 days, append the
phrase "short month" to the output. For months that contain 31 days,
append the phrase "long month" to the output.
