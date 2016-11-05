#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-09-07 16:23:57 -0400 (Mon, 07 Sep 2015) $
# $Revision: 81513 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab02/yards.bash $

if [[ $@ == "" ]]
then
	echo "Usage: yards.bash <filename>"
	exit 1
elif [[ ! -r $@ ]]
then
	echo "Error: $@ is not readable"
	exit 1
fi

Large=0
while read line || [[ -n "$line" ]]
do
    Conference=($line)
    N=0
    Ctotal=0
    for I in ${Conference[*]}
    do
	CName=${Conference[0]}
	if (( $N != 0 ))
	then
	    ((Ctotal+=$I))
	fi
	((N++))
    done
    ((Cavg=Ctotal/(N-1)))
    n=0
    Vtotal=0
    for I in ${Conference[*]}
    do
	if (( $n != 0 ))
	then
	    ((Vtotal+=($I-$Cavg)*($I-$Cavg)))
	fi
	((n++))
    done
    ((Var=Vtotal/(n-1)))
    echo "$CName schools averaged $Cavg yards receiving with a variance of $Var"
if (( $Large < $Cavg ))
then
    Large=$Cavg
fi
done < $1

echo "The largest average yardage was $Large"

exit 0