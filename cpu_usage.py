#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2018 Paul Short

import sys
import time

"""""
Given a function called “get_cpu” that takes a hostname as the only parameter and then returns the current CPU usage by 
percentage as an integer.  Write a script (in your language for choice) that does the following:

1) Accepts a hostname as a single parameter
2) For that host:
  a. Collects the current CPU usage once a minute over a time span of 1 hour
  b. Display the average CPU usage for that time period
  c. Display the time of the largest spike in CPU usage
  
Note: I wrote this in an IDE than copied over to the test box
"""

# Program Constants
NUMBER_OF_ITEMS = 60
SECONDS_TO_SLEEP = 60

# stub function to return the CPU usage
def get_cpu(hostname):
    return 50


class cpu_usage(self):
    max = 0
    max_time = 0
    count = 0   # The number of items in the array
    total = 0   # The sum of all the existing elements
    first = 0
    last = 0
    hostname = ''
    data = []

    def __init__(self, hostname):
        self.hostname = hostname
        return

    # get the CPU usage and update stats, store in a circular array
    def run(self):
        self.last = get_cpu(self.hostname)

        # as the array is being filled, need to handle differently than when array is filled
        if self.count != NUMBER_OF_ITEMS:
            self.data.append(self.last)
            if self.last > self.max:
                self.max = self.last
                self.max_time = int(time.time())
            self.count += 1
        else:
        # the array is filled, push and item into the array while poping the last item off
            self.first = self.data.pop(0)
            self.data.append = self.last
            self.total -= self.first  #remove from total

            # check for a new maxium and if the old maximum is removed
            if self.last > self.max:
                self.max = self.last
                self.max_time = int(time.time())
            else:
                # we removed the maximum, calculate a new maxium
                if self.first == self.max:
                    self.max = get_max_item()

        # update the total of the elements and return the average
        self.total += self.last
        return self.total/self.count

    # Walk through all the data and grab the maximum item, also reset the time it was collected
    def get_max_item(self):
        self.max = 0
        i = 0
        for value in self.data:
            if value > self.max:   # found a new maximum, also adjust the time based on the position in the array
                self.max = value
                tm = int(time.time())
                self.max_time = tm - (NUMBER_OF_ITEMS - i)*360
            i += 1
        return self.max

    def printstats(self):
        print("Average CPU: %d  Maximum CPU: %d  Peak time: %s",
              self.total/self.count, self.max, time.ctime(int(self.max_time)))



# Main
if __name__ == '__main__':

    cpu = cpu_usage(sys.argv[1])

    while True:
        cpu.run()
        cpu.printstats()
        time.sleep(SECONDS_TO_SLEEP)











