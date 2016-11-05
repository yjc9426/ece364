#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 18:32:51 -0400 (Mon, 31 Aug 2015) $
# $Revision: 80788 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/sum.bash $

Num_Of_Para=$#
Para_Values=$@

sum=0
for I in $Para_Values
do
    ((sum+=I))
done
echo $sum

exit 0