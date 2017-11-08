#!/usr/bin/python

import sys
cnt=0
old="GET"



for line in sys.stdin:
	line=line.strip()
	if line!=old:
		print old," ",cnt
		old=line
		cnt=1
	else:
		cnt+=1
print old," ",cnt
