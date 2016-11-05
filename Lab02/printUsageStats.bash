#! /bin/bash
#
#$Author: ee364b11 $
#$Date: 2016-01-26 15:10:01 -0500 (Tue, 26 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab02/printUsageStats.bash $
#$Revision: 86913 $
#$Id: printUsageStats.bash 86913 2016-01-26 20:10:01Z ee364b11 $

if [[ $# != 1 ]]
then
    echo "Usage: printUsageStats.bash <file name>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 not exist"
    exit 2
else
    tstamp=$(head -n 1 $1 | tail -c +6 | head -c 8)
    num=$(head -n 1 $1 | cut -d',' -f3 | head -c -6 | tail -c +1)
    (tail -n +8 $1)>tempfile
    echo "Parsing file \"$1\". Timestamp: $tstamp"
    echo "Your choices are:"
    echo "1) Active user IDs"
    echo "2) N Highest CPU usages"
    echo "3) N highest mem usages"
    echo "4) Top 3 longest running processes"
    echo "5) All processes by a specific user"
    echo "6) Exit"
    echo
    choice=0
    while [[ $choice != 6 ]] 
    do
	read -p "Please enter your choice: " choice 
	if [[ $choice == 1 ]]
	then
	    echo "Total number of active user IDs: $num"
	    echo
	elif [[ $choice == 2 ]]
	then
	    read -p "Enter a value for N:" N
	    user=($(sort -r -n -k9,9 tempfile | cut -d" " -f2))
	    cpu=($(sort -r -n -k9,9 tempfile | cut -d" " -f9))
	    ct=0
	    while [[ $N != 0 ]]
	    do
		echo "User ${user[ct]} is utilizing CPU resources at ${cpu[ct]}%"
		((ct++))
		((N--))
	    done
	    echo
	elif [[ $choice == 3 ]]
	then
	    read -p "Enter a value for N:" N
	    user=($(sort -r -n -k10,10 tempfile | cut -d" " -f2))
	    mem=($(sort -r -n -k10,10 tempfile | cut -d" " -f10))
	    ct=0
	    while [[ $N != 0 ]]
	    do
		echo "User ${user[ct]} is utilizing mem resources at ${mem[ct]}%"
		((ct++))
		((N--))
	    done
	    echo
	elif [[ $choice == 4 ]]
	then
	    pid=($(sort -r -n -k11,11 tempfile | cut -d" " -f1))
	    cmd=($(sort -r -n -k11,11 tempfile | cut -d" " -f12))
	    ct=0
	    while [[ $ct != 3 ]]
	    do
		echo "PID: ${pid[ct]}, cmd: ${cmd[ct]}"
		((ct++))
	    done
	    echo	    
	elif [[ $choice == 5 ]]
	then
	    read -p "Please enter a valid username: " name
	    cmd=($(grep -i $name tempfile | cut -d" " -f12))
	    cpu=($(grep -i $name tempfile | cut -d" " -f1))
	    c=0
	    if [[ ${#cmd[*]} == 0 ]]
	    then
		echo "No match found"
	    else
	    for n in ${cmd[*]}
	    do
		echo "${cpu[c]} $n"
	    done
	    fi
	elif [[ $choice == 6 ]]
	then
	    rm tempfile
	fi
    done
fi

exit 0	
      

	

