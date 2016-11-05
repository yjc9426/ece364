#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-09-07 22:15:39 -0400 (Mon, 07 Sep 2015) $
# $Revision: 81549 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab02/run.bash $

gcc $1 -o quick_sim

if [ $? != 0 ]
then
    echo "error: quick_sim could not be compiled!"
    exit 1
fi

if (( $# != 2 ))
then
    echo "Usage: run.bash <source file> <file name>"
    exit 1
fi

Csize=(1 2 4 8 16 32)
Isize=(1 2 4 8 16)
Proc=(a i)
filename=$2

if [[ -e $filename ]]
then
    read -p "$filename exists. Would you like to delete it? " delete
    if [[ $delete == "y" ]]
    then 
	rm $filename
    elif [[ $delete == "n" ]]
    then
	read -p "Enter a new filename: " fn
	filename=$fn
    fi
fi

for i in ${Csize[*]}
do
    for j in ${Isize[*]}
    do
	for k in ${Proc[*]} 
	do
	    quick_sim $i $j $k | cut -d":" -f2,4,6,8,10 >>$filename
	done
    done
done

    IFS=":"
    speed=($(sort -t":" -k5 -n $filename | head -n1))
    echo "Fastest run time achieved by ${speed[0]} with cache size ${speed[1]} and issue width ${speed[2]} was ${speed[4]}"
exit 0