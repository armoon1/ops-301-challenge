#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/05/2023
# Purpose:                      Directory Creation
 

# Import libraries
import os

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        # Add a print command here to print ==root==
        print(f"Root: {root}")
        # Add a print command here to print ==dirs==
        print(f"Directories: {dirs}")
        # Add a print command here to print ==files==
        print(f"Files: {files}")

# Main
if __name__ == "__main__":
    # Read user input here into a variable
    user_path = input("Enter the directory path: ")

    # Pass the variable into the function here
    generate_directory_structure(user_path)

