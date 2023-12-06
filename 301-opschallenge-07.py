#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/05/2023
# Purpose:                      Import libraries
 

import os

# Declaration of variables

### Read user input here into a variable

# Declaration of functions

### Declare a function here

for (root, dirs, files) in os.walk("testdir"):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

# Main

### Pass the variable into the function here

# End
