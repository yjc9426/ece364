#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-02-16 14:49:34 -0500 (Tue, 16 Feb 2016) $
# $Revision: 88216 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab05/practical1.py $

#!/usr/local/bin/python3.4

import sys
import math
import glob

def rowSumIsValid(mat):
    c=0
    s=sum(mat[0])
    print(s)
    for l in mat:
        temp=0
        for n in l:
            temp+=n
        c+=1
        if c > 1:
            if s != temp:
                return False
    return True

def columnSumIsValid(mat):
    c=0
    cs=[]
    for l in mat:
       c+=1
    while c != 0:
        cs.append(0)
        c-=1
    print(cs)
    for l in mat:
        c=0
        for n in l:
            cs[c]+=n
            c+=1
    temp = cs[0]
    for i in cs:
        if i != temp:
            return False
    return True

def magicSquareIsValid(filePath):
    with open(filePath,'r') as myFile:
        all_lines = myFile.readlines()
        l=[]
        mat=[]
        for line in all_lines:
            l=line.split()
            c=0
            for i in l:
                l[c]=int(i)
                c+=1
            mat.append(l)
        if rowSumIsValid(mat) == True and columnSumIsValid(mat) == True:
            return True
        return False

def getPrice():
    files=glob.glob("Stores/*")
    bdic={}
    for f in files:
        dic={}
        with open(f,'r') as myFile:
            all_lines = myFile.readlines()[3:]
            filename=f[7:-4]
            for line in all_lines:
                NP=line.split(',')
                dic[NP[0].strip()]=float(NP[1].strip()[1:])
            bdic[filename]=dic
    return bdic

def getTotalCost(itemSet):
    store=getPrice()
    dic={}
    for key in store:
        dic[key]=0
        print(key)
    for t in itemSet:
        cpu=t[0]
        qua=t[1]
        for key in store:
            dic[key]+=store[key][cpu]*qua
            dic[key]=round(dic[key],2)
    return dic

def getBestPrices(cpuSet):
    store=getPrice()
    dic={}
    for cpu in cpuSet:
        price=999999
        name=''
        for key in store:
            if cpu in store[key]:
                if store[key][cpu] < price:
                    price = store[key][cpu]
                    name=key
        dic[cpu]=(price,name)
    return dic

def getMissingItems():
    store=getPrice()
    dic={}
    nodic={}
    for key in store:
        dic[key]=[]
        nodic[key]=set()
        for cpu in store[key]:
            dic[key]+=[cpu]
    for key in store:
        for cpu in store[key]:
            for k in dic:
                if cpu not in dic[k]:
                    nodic[k].add(cpu)
    print(nodic)
    return nodic



if __name__ == "__main__":
    getPrice()
    a=[1,2,3]
    b=[4,5,6]
    print(a+b)