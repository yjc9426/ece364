#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import sys,os,math

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: parse.py [filename]')
    else:
        try:
            file = open(sys.argv[1],'r')
            all_line = file.readlines()
            print(all_line[0][:-1])
            for line in all_line[1:]:
                line = line.split()
                sum = 0.0
                n = 0
                string = ''
                for i in line:
                    try:
                        sum += float(i)
                        n += 1
                    except ValueError:
                        string += i + " "
                print("%.3f" %round(sum/n,3),string[:-1])
            file.close()
        except IOError:
            print("{} is not a readable file.".format(sys.argv[1]))