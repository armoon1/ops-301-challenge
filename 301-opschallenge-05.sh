#!/bin/bash
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/03/2023
# Purpose:                      Clearing Logs

# Write a bash script that performs the following tasks:

# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
# Hint: gzip is a preinstalled Linux application for performing zip formatted compression.

# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files

function check_file_size(){
    :
    # Print file_size
}
function compress_log_file(){
    :
    # Print compress_file
}