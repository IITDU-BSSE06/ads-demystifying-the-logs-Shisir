#!/usr/bin/python

#>>> a='http://www.the-associates.co.uk/images/filmmediablock/332/RtB_0576.jpg'
#>>> b=urlparse(a).path
#>>> b
#'/images/filmmediablock/332/RtB_0576.jpg'


import sys

from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        print urlparse(data[6]).path

