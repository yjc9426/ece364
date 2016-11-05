#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-03-08 15:25:59 -0500 (Tue, 08 Mar 2016) $
# $Revision: 89578 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab08/netConverter.py $

import sys
import HardwareTasks

def verilog2vhdl(ver_line):
    try:
        t = HardwareTasks.processLine(ver_line)
        l = list(t)
        s=l[1]+": "+l[0]+" PORT MAP("
        l2=list(l[2])
        for i in l2:
            a=list(i)
            s+=a[0]+"=>"+a[1]+", "
        s=s[:-2]
        s+=");"
    except ValueError:
        return "Error: Bad Line."
    return s

def convertNetlist(sourceFile, targetFile):
    file = open(sourceFile,'r')
    file2=open(targetFile,'w')
    all_line=file.readlines()
    s=""
    for line in all_line:
        s+=verilog2vhdl(line)+"\n"
    print(s[:-1])
    file2.write(s[:-1])
    file.close()
    file2.close()

