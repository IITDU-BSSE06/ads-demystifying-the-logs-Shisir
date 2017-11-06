#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print urlparse(data[6]).path
		#Using data[6].split("?")[0], it prints "filepath" same but different count(263712)
