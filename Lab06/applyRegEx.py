#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-02-29 11:51:33 -0500 (Mon, 29 Feb 2016) $
# $Revision: 89006 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab06/applyRegEx.py $

import math
import re
import sys

def getRejectedUsers():
    file = open('SiteRegistration.txt','r')
    all_lines= file.readlines()
    name=[]
    exp1="([\w]+,?\s?[\w]+)"
    exp2="([\w.-]+@[\w.-]+)"
    exp3="([0-9]+(\)?\s?-?)[0-9]+(-?)[0-9]+)"
    exp4="(,[A-Z][a-z]+)"
    for line in all_lines:
        m1=re.match(exp1,line)
        m2=re.search(exp2,line)
        m3=re.search(exp3,line)
        m4=re.search(exp4,line)
        if m1 and not m2 and not m3 and not m4:
            if re.match("([\w]+,?\s?[\w]+)",line):
                s=re.match("([\w]+)(,?\s?)([\w]+)(,*;*\s*)",line)
                print(s.group(0))
                if re.match("([\w]+)(,\s)([\w]+)",line):
                    m=re.match("([\w]+)(,\s)([\w]+)",line)
                    name.append(m.group(3)+" "+m.group(1))
                else:
                    m=re.match("([\w]+)(\s)([\w]+)",line)
                    name.append(m.group(1)+" "+m.group(3))
    return sorted(name)

def getUsersWithEmails():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    dic={}
    exp1="([\w]+,?\s?[\w]+)"
    exp2="([\w.-]+@[\w.-]+)"
    for line in all_lines:
        m1=re.match(exp1,line)
        m2=re.search(exp2,line)
        if m1 and m2:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                dic[name]=m2.group(0)
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                dic[name]=m2.group(0)
    return dic

def getUsersWithPhones():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    dic={}
    exp1="([\w]+,?\s?[\w]+)"
    exp3="(\(?([0-9]{3})\)?\s?-?([0-9]{3})-?([0-9]{4}))"
    for line in all_lines:
        m1=re.match(exp1,line)
        m3=re.search(exp3,line)
        if m1 and m3:
            print(m3.group(0))
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                dic[name]="("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4)

            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                dic[name]="("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4)
    return dic

def getUsersWithStates():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    dic={}
    exp1="([\w]+,?\s?[\w]+)"
    exp4="([A-Z][a-z]+)"
    for line in all_lines:
        m1=re.match(exp1,line)
        m4=re.search(exp4,line)
        ma=re.findall(exp4,line)
        if len(ma)>2:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                if len(ma)==3:
                    dic[name]=ma[2]
                else:
                    dic[name]=ma[2]+" "+ma[3]
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                if len(ma)==3:
                    dic[name]=ma[2]
                else:
                    dic[name]=ma[2]+" "+ma[3]

    return dic

def getUsersWithoutEmails():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    n=[]
    exp1="([\w]+,?\s?[\w]+)"
    exp2="([\w.-]+@[\w.-]+)"
    rej=getRejectedUsers()
    for line in all_lines:
        m1=re.match(exp1,line)
        m2=re.search(exp2,line)
        if m1 and not m2:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                if name not in rej:
                    n.append(name)
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                if name not in rej:
                    n.append(name)
    return sorted(n)

def getUsersWithoutPhones():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    n=[]
    exp1="([\w]+,?\s?[\w]+)"
    exp3="(\(?([0-9]{3})\)?\s?-?([0-9]{3})-?([0-9]{4}))"
    rej=getRejectedUsers()
    for line in all_lines:
        m1=re.match(exp1,line)
        m3=re.search(exp3,line)
        if m1 and not m3:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                if name not in rej:
                    n.append(name)
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                if name not in rej:
                    n.append(name)
    return sorted(n)

def getUsersWithoutStates():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    n=[]
    exp1="([\w]+,?\s?[\w]+)"
    exp4="([A-Z][a-z]+)"
    rej=getRejectedUsers()
    for line in all_lines:
        m1=re.match(exp1,line)
        m4=re.findall(exp4,line)
        if m1 and len(m4)<=2:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                if name not in rej:
                    n.append(name)
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                if name not in rej:
                    n.append(name)
    return sorted(n)

def getUsersWithCompleteInfo():
    file = open('SiteRegistration.txt','r')
    all_lines=file.readlines()
    dic={}
    for line in all_lines:
        exp1="([\w]+)(,?\s?)([\w]+)"
        exp2="([\w.-]+@[\w.-]+)"
        exp3="(\(?([0-9]{3})\)?\s?-?([0-9]{3})-?([0-9]{4}))"
        exp4="([A-Z][a-z]+)"
        m1= re.match(exp1,line)
        m2= re.search(exp2,line)
        m3= re.search(exp3,line)
        m4= re.findall(exp4,line)
        if m1 and m2 and m3 and len(m4)>2:
            if re.match("([\w]+)(,\s)([\w]+)",line):
                m=re.match("([\w]+)(,\s)([\w]+)",line)
                name=m.group(3)+" "+m.group(1)
                if len(m4)==3:
                    dic[name]=(m2.group(0),"("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4),m4[2])
                else:
                    dic[name]=(m2.group(0),"("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4),m4[2]+" "+m4[3])
            else:
                m=re.match("([\w]+)(\s)([\w]+)",line)
                name=m.group(1)+" "+m.group(3)
                if len(m4)==3:
                    dic[name]=(m2.group(0),"("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4),m4[2])
                else:
                    dic[name]=(m2.group(0),"("+m3.group(2)+") "+m3.group(3)+"-"+m3.group(4),m4[2]+" "+m4[3])
    return dic

