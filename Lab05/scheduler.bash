#! /bin/bash
#
#$Author: ee364b11 $
#$Date: 2016-02-16 15:20:15 -0500 (Tue, 16 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab05/scheduler.bash $
#$Revision: 88260 $
#$Id: scheduler.bash 88260 2016-02-16 20:20:15Z ee364b11 $

if (( $# != 1 ))
then
    echo "Usage: ./scheduler.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readbale"
    exit 2
else
    t=(7:00 8:00 9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00)
    echo ${t[*]}>schedule.out
    while read line
    do
	name=($(echo $line | cut -d" " -f1) "-    " '-    ' '-    ' '-    ' '-    ' '-    ' '-    ' '-    ' '-    ' '-    ' '-    ')
	
	time=($(echo $line | cut -d" " -f2 | cut -d"," -f1))
	echo ${name[*]} >>schedule.out
    done<$1
    exit 0
fi