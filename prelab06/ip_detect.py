#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import math
import re
import sys

file = open('addys.in','r')
all_lines = file.readlines()
for line in all_lines:
    ip_port = re.split(':',line)
    if re.match("^([1][0-9][0-9].|^[2][5][0-5].|^[2][0-4][0-9].|^[0][0-9][0-9].|^[0-9][0-9].|^0?0?[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[0][0-9][0-9].|[0-9][0-9].|0?0?[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[0][0-9][0-9].|[0-9][0-9].|0?0?[0-9].)([1][0-9][0-9]|[2][5][0-5]|[2][0-4][0-9]|[0][0-9][0-9]|[0-9][0-9]|[0-9]|00[0-9])$",ip_port[0]):
            if re.search('[a-zA-Z]+',ip_port[1]) or int(ip_port[1]) > 32767 or int(ip_port[1]) < 1 :
                result = line[:-1] + " - Invalid Port Number"
            else:
                result = line[:-1] + " - Valid"
                if int(ip_port[1]) < 1024:
                    result += " (root privileges required)"
    else:
            result = line[:-1] + " Invalid IP Address"
    print(result)

