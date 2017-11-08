#!/usr/bin/python

import sys
cnt=0
old=None
total=0
result=None


for line in sys.stdin:
	line=line.strip().split("%")[0]
	if line!=old:
		if total<cnt:
			total=cnt
			result=old
		old=line
		cnt=1
	else:
		cnt+=1
if total<cnt:
	total=cnt
	result=old
print result," ",total
