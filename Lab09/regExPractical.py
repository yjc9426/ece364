#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-03-22 15:18:07 -0400 (Tue, 22 Mar 2016) $
# $Revision: 89779 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab09/regExPractical.py $

import math
import re
import sys

def getAddress(sentence):
    exp="[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}"
    exp2="[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}"
    m=re.findall(exp,sentence)
    m2=re.findall(exp2,sentence)
    print(m)
    if m:
        return m[0]
    elif m2:
        return m2[0]
    else:
        return None

def getSwitches(commandline):
    l=[]
    exp=r"(\+[a-z]{1}\s+)([^\+\\]+)"
    exp2=r"(\\[a-z]{1}\s+)([^\+\\]+)"
    m=re.findall(exp,commandline)
    m2=re.findall(exp2,commandline)
    if m:
        for t in m:
            a=(list(t)[0].strip())[1:]
            if t[1] != " ":
                l.append((a,t[1].strip()))
    if m2:
        for t in m2:
            a=(list(t)[0].strip())[1:]
            if t[1] != " ":
                l.append((a,t[1].strip()))
    print(l)
    return sorted(l)

def getElements(fullAddress):
    exp="(http://)([\w+.?]+)(/)([a-zA-Z0-9]+)(/)([a-zA-Z0-9]+)$"
    exp2="(https://)([\w+.?]+)(/)([a-zA-Z0-9]+)(/)([a-zA-Z0-9]+)$"
    m=re.match(exp,fullAddress)
    m2=re.match(exp2,fullAddress)
    if m:
        return (m.group(2),m.group(4),m.group(6))
    elif m2:
        return (m2.group(2),m2.group(4),m2.group(6))
    else:
        return None

