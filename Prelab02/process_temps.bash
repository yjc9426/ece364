#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-09-07 16:31:26 -0400 (Mon, 07 Sep 2015) $
# $Revision: 81515 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab02/process_temps.bash $

if (( $# != 1 ))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
elif [[ ! -r $@ ]]
then
    echo "Error: $@ is not a readable file."
    exit 2
else
    n=0
    while read line || [[ -n "$line" ]]
    do
	IFS=$'\t'
	Arr=($line)
	if (( $n != 0 ))
	then
	    k=0
	    sumT=0
            for I in ${Arr[*]}
	    do
		if (( k != 0 ))
		then
		    ((sumT+=$I))
		fi
		((k++))
	    done
	    ((avgT=$sumT/(k-1)))
	    echo "Average temperature for time ${Arr[0]} was $avgT C."
	fi
	((n++))
    done < $@
fi
exit 0