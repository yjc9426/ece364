#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 23:41:02 -0400 (Mon, 31 Aug 2015) $
# $Revision: 81050 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/sensor_sum.sh $

if [[ $@ == "" ]]
then
    echo "usage: sensor_sum.sh"
elif [[ ! -r $@ ]]
then
    echo "error: $@ is not a readable file!"
else

SensorID=($( cut -f1 $@ ))
N0=($( cut -f2 $@ ))
N1=($( cut -f3 $@ ))
N2=($( cut -f4 $@ ))

k=0
for I in ${SensorID[*]}
do
    ((sum=${N0[k]}+${N1[k]}+${N2[k]}))
    echo "$I $sum"
    ((k++))
done
fi

exit 0