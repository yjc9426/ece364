#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 20:06:42 -0400 (Mon, 31 Aug 2015) $
# $Revision: 80845 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/exist.bash $

Values=$@
Num=$#

for I in $@
do
    if [[ -r $I ]]
    then
        echo "File $I is readable!"
    else
	touch $I
    fi
done

exit 0