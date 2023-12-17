#!/bin/bash
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/03/2023
# Purpose:                      Clearing Logs

# Write a bash script that performs the following tasks:

# Set the backup directory
backup_dir="/var/log/backups"

# Function to print file size
print_file_size() {
    echo "File size of $1: $(du -h $1 | cut -f1)"
}

# Print original file sizes
echo "Original file sizes before compression:"
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# Create timestamp for the compressed file
timestamp=$(date "+%Y%m%d%H%M%S")

# Compress log files to backup directory
gzip -c /var/log/syslog > "$backup_dir/syslog-$timestamp.gz"
gzip -c /var/log/wtmp > "$backup_dir/wtmp-$timestamp.gz"

# Clear the contents of the log files
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Print compressed file sizes
echo -e "\nCompressed file sizes:"
print_file_size "$backup_dir/syslog-$timestamp.gz"
print_file_size "$backup_dir/wtmp-$timestamp.gz"

# Compare sizes
echo -e "\nSize comparison:"
echo "Original syslog size vs Compressed syslog size:"
cmp_size=$(cmp -l "/var/log/syslog" "$backup_dir/syslog-$timestamp.gz" | wc -l)
echo "Number of different bytes: $cmp_size"

echo -e "\nOriginal wtmp size vs Compressed wtmp size:"
cmp_size=$(cmp -l "/var/log/wtmp" "$backup_dir/wtmp-$timestamp.gz" | wc -l)
echo "Number of different bytes: $cmp_size"
