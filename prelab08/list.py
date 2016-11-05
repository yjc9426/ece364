#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import sys,math,os,traceback

def find_median(fstList,sndList):
    allList = fstList + sndList
    ind = int(len(allList)/2) - 1
    med = sorted(allList)[ind]
    return (med,sorted(allList))

if __name__ == "__main__":
    first = input('Enter the first list of numbers: ').split()
    second = input('Enter the second list of numbers: ').split()
    fstList = []
    for i in first:
        fstList.append(int(i))
    sndList = []
    for j in second:
        sndList.append(int(j))
    (med,sorted_List) = find_median(fstList,sndList)
    print("First list: ", fstList)
    print("Second list: ", sndList)
    print("Merged list: ", sorted_List)
    print("Median: ", med)