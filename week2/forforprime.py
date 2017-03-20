#!/usr/bin/env python #!/usr/bin/env python
# week 2 - example 4, nested for loops to find prime numbers

num = range(2, 20)  # change range to check as desired

for n in num:  # check each n in range to see if is prime
    for x in range(2, n):  # divide each n(umber) by all lower numbers from 2 up
        if n % x == 0:  # if modulo n/x is 0, no remainder, then not prime
            print("{:4d} is NOT a prime number".format(n))
            break  # no point looking at higher values of x

    else:  # nobreak - i.e. what to do if iter completed without match
        print("{:4d} is     a prime number".format(n))  # didn't break, must be prime
