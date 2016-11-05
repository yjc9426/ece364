#! /bin/bash
#
#$Author: ee364b11 $
#$Date: 2016-01-19 15:22:56 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab01/getCourseStats.bash $
#$Revision: 86205 $
#$Id: getCourseStats.bash 86205 2016-01-19 20:22:56Z ee364b11 $

if (( $# != 1 ))
then
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1
fi
if [[ $1 == "ece364" ]] || [[ $1 == "ece337" ]] || [[ $1 == "ece468" ]]
then
    for file in $(ls gradebooks/$1*.txt)
    do
        ./getFinalScores.bash $file
	if (( $? != 0 ))
	then
	    echo "Error while running getFinalScores.bash"
	    exit 3
	fi
    done
    total=0
    score=0
    high=0
    for ofile in $(ls gradebooks/$1*.out)
    do
	((total=$total + $(cat $ofile | wc -l)))
	while read line
	do
	    ((score+=$(echo $line | cut -d',' -f2)))
	    if (( high < $(echo $line | cut -d',' -f2) ))
	    then
		high=$(echo $line | cut -d',' -f2)
		name=$(echo $line | cut -d',' -f1)
	    fi
	done<$ofile
    done
    ((avg=$score/$total))
    echo "Total student: $total"
    echo "Average score: $avg"
    echo "$name had the highest score of $high"
    exit 0
else
    echo "Error: course $1 is not a valid option."
    exit 5
fi