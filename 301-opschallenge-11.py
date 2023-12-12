#!/usr/bin/env python3
# Author:                       SEYED MEHDI HASHEMI SOHI
# Date of latest revision:      12/11/2023
# Purpose:                      Ops 11

import psutil
# creating function
def get_system_info():
# Time spent by normal processes executing in user mode
    cpu_times = psutil.cpu_times()
# Time spent by normal processes executing in user mode
    user_mode_time = cpu_times.user
# Time spent by processes executing in kernel mode
    kernel_mode_time = cpu_times.system
# Time when system was idle
    idle_time = cpu_times.idle
# Time spent by priority processes executing in user mode
    priority_user_mode_time = cpu_times.nice
# Time spent waiting for I/O to complete.
    io_wait_time = cpu_times.iowait
# Time spent for servicing hardware interrupts
    hardware_interrupt_time = cpu_times.irq
# Time spent for servicing software interrupts
    software_interrupt_time = cpu_times.softirq
# Time spent by other operating systems running in a virtualized environment
    virtual_environment_time = cpu_times.steal
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
    guest_time = cpu_times.guest

    # Print the information
    print(f"Time spent by normal processes executing in user mode: {user_mode_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {kernel_mode_time} seconds")
    print(f"Time when the system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {priority_user_mode_time} seconds")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {hardware_interrupt_time} seconds")
    print(f"Time spent for servicing software interrupts: {software_interrupt_time} seconds")
    print(f"Time spent by other operating systems running in a virtualized environment: {virtual_environment_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds")

if __name__ == "__main__": # cjecking if it is run as main program
    get_system_info()
