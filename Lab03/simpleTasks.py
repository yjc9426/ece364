#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-02-02 14:40:43 -0500 (Tue, 02 Feb 2016) $
# $Revision: 87518 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab03/simpleTasks.py $

#! /usr/bin/env python3.4

import sys

def getPairwiseDifference(vec):
    newlist=[]
    if type(vec) is not list:
        return None
    elif vec == []:
        return None
    else:
        for i in range(len(vec)-1):
            newlist.append(vec[i+1]-vec[i])
        return newlist

def flatten(l):
    newlist=[]
    if type(l) is not list:
        return None
    elif l == []:
        return None
    else:
        for i in l:
            if type(i) is not list:
                return None
            else:
                newlist.extend(i)
        return newlist

def partition(l,n):
    newlist=[]
    val=[]
    if type(l) is not list:
        return None
    elif l == []:
        return None
    else:
        for i in range(0,len(l),n):
            newlist.append(l[i:i+n])
        return newlist

def rectifySignal(signal):
    newlist=[]
    if type(signal) is not list:
        return None
    elif signal == []:
        return None
    else:
        for i in signal:
            if i > 0:
                newlist.append(i)
            else:
                newlist.append(0)
        return newlist

def floatRange(a,b,s):
    if a<b:
        newlist=[]
        temp=float(a)
        while temp != float(b):
            newlist.append(temp)
            temp=round(temp+s,1)
        newlist.append(float(b))
        return newlist
    else:
        return None

def getLongestWord(sentence):
    if type(sentence) is not str:
        return None
    else:
        s=sentence.split()
        if len(s)>1:
            w=''
            for i in s:
                if len(w)<len(i):
                    w=i
            return w
        else:
            return None

def decodeNumbers(numList):
    s=''
    if type(numList) is not list:
        return None
    else:
        for i in numList:
            if type(i) is not int:
                return None
            s+=chr(i)
        return s

def getCreditCard(s):
    newlist=[]
    if s != '':
        for l in s:
            if 48<=ord(l) and ord(l)<=57:
                newlist.append(int(l))
        return newlist



if __name__ == "__main__":
    l=[1,2,3,4,5,6,7]
    m=['aaa']
    if type(l) is not list:
        print('not list')
    elif l == []:
        print('empty')
    print(partition(l,3))
    print(floatRange(1,2,.1))
    print(ord('1'))