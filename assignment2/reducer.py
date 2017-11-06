#!/usr/bin/python

import sys
cnt=0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	jsdata=line.strip()
	if jsdata=="/assets/js/the-associates.js":
		cnt+=1
print cnt," hits were made to /assets/js/the-associates.js"
