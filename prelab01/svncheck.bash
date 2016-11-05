#! /bin/bash
#
# $Author: ee364c08 $
# $Date: 2015-08-31 20:55:54 -0400 (Mon, 31 Aug 2015) $
# $Revision: 80883 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364c08/Prelab01/svncheck.bash $

if [[ $@ == "" ]]
then
    echo "usage: svncheck.bash <filenamelist>"
else

while read line || [[ -n "$line" ]]
do
    filename+=($line)
done < $@

for I in ${filename[*]}
do
    SVN_STATUS=$(svn status $I | head -c 1)
    if [[ -e $I ]] && [[ SVN_STATUS != "" ]]
    then
        if [[ ! -x $I ]]
        then
            echo "Do you want to make $I executable? y/n"
            read Input
            if [[ Input == "y" ]]
            then
    	        chmod +x $file
            fi
        fi
        svn add $I
    elif [[ SVN_STATUS == "" ]] && [[ ! -e $I ]]
    then
	if [[ ! -x $I ]]
        then
            svn propset svn:executable ON $I
        fi
    else [[ SVN_STATUS != "" ]] && [[ ! -e $I ]]
        echo "Error:File $I appears to not exist here or in svn"
	
    fi 
done

fi

exit 0