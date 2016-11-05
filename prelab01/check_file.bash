#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 20:54:32 -0400 (Mon, 31 Aug 2015) $
# $Revision: 80881 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/check_file.bash $

if [[ $@ == "" ]]
then
    echo "Usage: ./check_file.bash <filename>"
fi

for I in $@
do
    if [[ -e $I ]]
    then
        echo "$I exists"
    else
        echo "$I does not exist"
    fi

    if [[ -d $I ]]
    then
        echo "$I is a directory"
    else
        echo "$I is not a directory"
    fi

    if [[ -f $I ]]
    then
        echo "$I is an ordinary file"
    else
        echo "$I is not an ordinary file"
    fi

    if [[ -r $I ]]
    then
        echo "$I is readable"
    else
        echo "$I is not readable"
    fi

    if [[ -w $I ]]
    then
        echo "$I is writable"
    else
        echo "$I is not writable"
    fi

    if [[ -x $I ]]
    then
        echo "$I is executable"
    else
        echo "$I is not executable"
    fi
done

exit 0