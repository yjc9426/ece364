#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-02-09 14:41:02 -0500 (Tue, 09 Feb 2016) $
# $Revision: 87945 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab04/registrar.py $

#!/usr/local/bin/python3.4

import sys
import math
import glob
import string

def getNames():
    dic = {}
    with open("files/students.txt",'r') as myFile:
        all_lines = myFile.readlines()[2:]
        for line in all_lines:
            nameID=line.split('|')
            dic[nameID[1].strip()]=nameID[0].strip()
    return dic



def getDetails():
    files = sorted(glob.glob("files/EECS*"))
    names = getNames()
    dic = {}
    for f in files:
        with open(f,'r') as myFile:
            course=f[10:13]
            all_lines = myFile.readlines()[2:]
            for line in all_lines:
                scoreID=line.split()
                if names[scoreID[0].strip()] in dic:
                    dic[names[scoreID[0].strip()]].add((course,int(scoreID[1].strip())))
                else:
                    dic[names[scoreID[0].strip()]]={(course,int(scoreID[1].strip()))}
    return dic

def getStudentList(classNumber):
    filename="files/EECS"+str(classNumber)+".txt"
    files=glob.glob("files/EECS*")
    names=getNames()
    namelist=[]
    if filename not in files:
        return namelist
    with open(filename,'r') as myFile:
        all_lines = myFile.readlines()[2:]
        for line in all_lines:
            ID=line.split()[0]
            namelist.append(names[ID])
    return sorted(namelist)

def searchForName(studentName):
    detail=getDetails()
    dic={}
    if studentName not in detail:
        return dic
    for t in detail[studentName]:
        dic[t[0]]=t[1]
    return dic

def searchForID(studentID):
    names=getNames()
    detail=getDetails()
    dic={}
    if studentID not in names:
        return dic
    n = names[studentID]
    for t in detail[n]:
        dic[t[0]]=t[1]
    return dic

def findScore(studentName, classNumber):
    namelist=getStudentList(classNumber)
    if studentName not in namelist:
        return None
    courseScore=searchForName(studentName)
    if courseScore == {}:
        return None
    return courseScore[classNumber]

def getHighest(classNumber):
    namelist=getStudentList(classNumber)
    if namelist == []:
        return ()
    score=0
    name=''
    for n in namelist:
        temp = findScore(n,classNumber)
        if score < temp:
            score = temp
            name = n
    return (name,float(score))

def getLowest(classNumber):
    namelist=getStudentList(classNumber)
    if namelist == []:
        return ()
    score=100
    name=''
    for n in namelist:
        temp = findScore(n,classNumber)
        if score > temp:
            score = temp
            name = n
    return (name,float(score))

def getAverageScore(studentName):
    courseScore = searchForName(studentName)
    if courseScore == {}:
        return None
    total=0
    num=0
    for key in courseScore:
        total+=courseScore[key]
        num+=1
    return total/num

if __name__ == "__main__":
    name = getNames()
    files=sorted(glob.glob("files/EECS*"))
    print(files)
    print(files[0][10:13])
    getStudentList(370)