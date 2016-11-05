#! /bin/bash
#
#$Author: ee364b11 $
#$Date: 2016-01-19 15:23:22 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab01/getFinalScores.bash $
#$Revision: 86206 $
#$Id: getFinalScores.bash 86206 2016-01-19 20:23:22Z ee364b11 $

if (( $# != 1 ))
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
fi
filename=$(echo $1 | cut -d'.' -f1 ).out
if [[ -e $filename ]]
then
	echo "Output file $filename already exists"
	exit 3
fi

if [[ ! -e $1 ]]
then
    echo "Error reading input file: $1"
    exit 2
else
while read line
do
    name=$(echo $line | cut -d',' -f1)
    assi=$(echo $line | cut -d',' -f2)
    mid1=$(echo $line | cut -d',' -f3)
    mid2=$(echo $line | cut -d',' -f4)
    proj=$(echo $line | cut -d',' -f5)
    ((score=15*$assi/100+ 30*$mid1/100+ 30*$mid2/100+25*$proj/100))
    echo "$name,$score">>$filename
done<$1
fi
exit 0