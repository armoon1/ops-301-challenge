#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/07/2023
# Purpose:                      Ops 09
#Create if statements using these logical conditionals below. 
#Each statement should print information to the screen depending on if the condition is met.

# Sample values for a and b
a = 10
b = 5

# If statement using equality
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
else:
    print("This should not happen, there's an issue with the conditions")

# If statement using less than
if a < b:
    print("a is less than b")
elif a >= b:
    print("a is greater than or equal to b")
else:
    print("This should not happen, there's an issue with the conditions")

# If statement using greater than
if a > b:
    print("a is greater than b")
elif a <= b:
    print("a is less than or equal to b")
else:
    print("This should not happen, there's an issue with the conditions")
