#!/usr/bin/env python
import os
import urllib 
import urllib2
import sys
file_dir=sys.argv[1]
#file_dir="http://111.42.183.93:181/all.tar.gz"
data=urllib2.urlopen(file_dir).read().strip()
#print(data)
with open("all.tar.gz","w") as fd:
    fd.write(data)

