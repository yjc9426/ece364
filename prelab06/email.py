#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import math
import re
import sys

file = open('Part2.in',"r")
all_lines = file.readlines()
for line in all_lines:
    if( re.match("([\w.-]+)@([\w.-]+)",line).group(2) == 'purdue.edu'):
        line = re.sub("purdue.edu","ecn.purdue.edu",line)
        num = str(re.search("[0-9]+\.[0-9]+",line).group(0)) + "/100"
        line = re.sub("[0-9]+\.[0-9]+",num,line)
        print(line)

file.close()
