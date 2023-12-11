#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/10/2023
# Purpose:                      Ops 10

#importing module
import os


# Create a new .txt file and append three lines
# with statement automatically close file when the block is exited.
# "w" for opening the file in write mode 
with open("new.txt", "w") as file: 
    file.write("First line.\n")
    file.write("Second line.\n")
    file.write("Third line.\n")

# Step 2: Read and print the first line from the file
with open("new.txt", "r") as file: # "r" for openinng in read mode
    first_line = file.readline()
    print("First line:", first_line)

# Step 3: Delete the .txt file
os.remove("new.txt")
