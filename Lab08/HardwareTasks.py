#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-03-08 15:25:42 -0500 (Tue, 08 Mar 2016) $
# $Revision: 89577 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab08/HardwareTasks.py $
import sys,string

def idIsAcceptable(ver_id):
    for i in ver_id:
        if i in string.ascii_letters or i in string.digits or i == "_":
            pass
        else:
            return False
    return True

def processSingle(ver_assignment):
    n=ver_assignment.split("(")
    t=[]
    if len(n) == 2:
        if n[0][0] == "." and idIsAcceptable(n[0][1:]):
            t.append(n[0][1:])
        else:
            raise ValueError(ver_assignment)
        if n[-1][-1] == ")" and idIsAcceptable(n[1][:-1]):
            t.append(n[1][:-1])
        else:
            raise ValueError(ver_assignment)
    else:
        raise ValueError(ver_assignment)
    return tuple(t)

def processLine(ver_line):
    n=ver_line.split()
    t=[]
    t2=[]
    if not idIsAcceptable(n[0]):
        raise ValueError(n[0])
    if not idIsAcceptable(n[1]):
        raise ValueError(n[1])
    t.append(n[0])
    t.append(n[1])
    if len(n) != 3:
        if n[2][0] != "(" or n[-1][-1] != ")":
            raise ValueError(ver_line)
        l=n[2:-1]
        s=""
        for i in l:
            s += i
        li=s[1:].split(",")
        for i in li:
            if processSingle(i):
                t2.append(processSingle(i))
    else:
        l=n[2][1:-1].split(",")
        print(l)
        for i in l:
            t2.append(processSingle(i))
    t.append(tuple(t2))
    return tuple(t)




if __name__ == "__main__":
    pass