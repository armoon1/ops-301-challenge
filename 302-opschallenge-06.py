#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/04/2023
# Purpose:                      Ops 06

# The Python module “os” must be utilized.
import os

# At least three variables must be declared and referenced in Python
username = 'whoami'
IP_Address = 'ip a'
lshw_short = 'lshw -short'
# Execute bash commands using os.popen()
def execute_bash_commands():

    result_whoami = os.popen(username).read()
    result_ip_a = os.popen(IP_Address).read()
    result_lshw_short = os.popen(lshw_short).read()
# Print the results
    print("Result of 'whoami' command:")
    print(result_whoami)

    print("\nResult of 'ip a' command:")
    print(result_ip_a)

    print("\nResult of 'lshw -short' command:")
    print(result_lshw_short)   

# Main
if __name__ == "__main__": 
    # Execute bash commands and print results
    execute_bash_commands()