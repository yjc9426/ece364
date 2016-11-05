#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import sys
import list

if __name__ == "__main__":
    first = input('Enter the first list of numbers: ').split()
    second = input('Enter the second list of numbers: ').split()
    fstList = []
    for i in first:
        fstList.append(int(i))
    sndList = []
    for j in second:
        sndList.append(int(j))
    (med,sorted_List) = list.find_median(fstList,sndList)
    print("First list: ", fstList)
    print("Second list: ", sndList)
    print("Merged list: ", sorted_List)
    print("Median: ", med)