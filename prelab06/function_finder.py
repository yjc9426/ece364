#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import re
import math
import sys
import os

if len(sys.argv) != 2:
    print("Usage: function_finder.py [python_file_name]")
elif os.access(sys.argv[1],os.R_OK):
    file = open(sys.argv[1],'r')
    all_lines = file.readlines()
    for line in all_lines:
        func_line = re.match("^(def)(.*)",line)
        if func_line:
            func = func_line.group(2).strip()
            func_name = re.search("(^\w+)",func)
            if func_name:
                print(func_name.group(1))
            arg = re.search("(\()(.*)",func)
            if arg:
                arg_name = re.split(",",arg.group(2)[:-2])
                ct = 1
                for name in arg_name:
                    print("Arg{1}: {0}".format(name.strip(),ct))
                    ct += 1
    file.close()
else:
    print("Error: Could not read {}" .format(sys.argv[1]))
