#!/usr/bin/python

import sys
cnt1=0
cnt2=0
cnt3=0

for line in sys.stdin:
	line=line.strip()
	if line=="2009":
		cnt1+=1
	elif line=="2010":
		cnt2+=1
	elif line=="2011":
		cnt3+=1
print "2009 ",cnt1
print "2010 ",cnt2
print "2011 ",cnt3
maxi=max(cnt1,max(cnt2,cnt3))
print "most number of hits: ",maxi
