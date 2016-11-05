#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 22:31:12 -0400 (Mon, 31 Aug 2015) $
# $Revision: 80998 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/line_num.bash $

Values=$@
Num=$#

if [[ $@ == "" ]]
then
    echo "Usage: line_num.bash <filename>"
elif [[ -r $@ ]]
then
    n=1
    while read line || [[ -n "$line" ]]
    do
        echo "$n:$line"
        ((n++))
    done < $@
else
    echo "Cannot read $I"
fi

exit 0