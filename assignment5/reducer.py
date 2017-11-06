#!/usr/bin/python

import sys
cnt=0
old=None
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	line=line.strip()
	if line!=old:
		old=line
		cnt+=1
print cnt," unique files are there."
