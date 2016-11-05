#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import sys

if __name__ == "__main__":
    list_str = input('Please enter some values: ').split()
    sum = 0.0
    for i in list_str:
        try:
            sum += float(i)
        except ValueError:
            pass
    print("The sum is: ", sum)