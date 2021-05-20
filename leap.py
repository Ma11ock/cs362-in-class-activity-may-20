#!/usr/bin/env python

# by Ryan Jeffrey
# Determines if the year entered is a leap year.

# From the directions:
# Years that are evenly divisible by 4 except
# years that are evenly divisible by 100
# unless the years are also evenly divisible by 400.

success = False
while not success:
    userInput = input("Enter the year: ")
    try:
        year = int(userInput)
        success = True
    except ValueError:
        print("%s is not valid user input" % userInput)

if year % 4 == 0 and (not (year % 100 == 0) or (year % 400 == 0)):
    print("%d is a leap year." % year)
else:
    print("%d is not a leap year." % year)
