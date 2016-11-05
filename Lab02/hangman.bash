#! /bin/bash
#
#$Author: ee364b11 $
#$Date: 2016-02-01 12:40:40 -0500 (Mon, 01 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab02/hangman.bash $
#$Revision: 87388 $
#$Id: hangman.bash 87388 2016-02-01 17:40:40Z ee364b11 $

(( pick=$RANDOM%3 ))
b=(b a n a n a)
p=(p a r s i m o n i o u s)
s=(s e s q u i p e d a l i a n)

if [[ $pick == 0 ]]
then
    temp=(. . . . .)
    echo "Your word is ${#b[*]} letters long."
    ct=0
    while [[ $ct != 3 ]]
    do
    echo "Word is: ${temp[*]}"	
    read -p "Make a guess: " guess
    if [[ $guess == b && ${temp[0]} != b ]]
    then
	echo "Good going!"
	temp[0]=b
	((ct++))
    elif [[ $guess == a && ${temp[1]} != a ]]
    then
	echo "Good going!"
	temp[1]=a
	temp[3]=a
	temp[5]=a
	((ct++))
    elif [[ $guess == n && ${temp[2]} != n ]]
    then
	echo "Good going!"
	temp[2]=n
	temp[4]=n
	((ct++))
    else
	echo "Sorry, try again!"
    fi
    
    done
    echo "Congratulation! You guessed the word: banana"

elif [[ $pick == 1 ]]
then
    temp=(. . . . . . . . . . . .)
    echo "Your word is ${#p[*]} letters long."
    ct=0
    while [[ $ct != 12 ]]
    do
	echo "Word is: ${temp[*]}"	
	read -p "Make a guess: " guess
	n=0
	bool=0
	for i in ${p[*]}
	do
	    if [[ $guess == $i && ${temp[$n]} != $guess ]]
	    then
		temp[$n]=$guess
		bool=1
		((ct++))
	    fi
	    ((n++))
	done
	if [[ $bool == 1 ]]
	then
	    echo "Good going!"
	else
	    echo "Sorry, try again!"
	fi
    done
    echo "Congratulation! You guessed the word: parsimonious"
else
    temp=(. . . . . . . . . . . . . .)
    echo "Your word is ${#s[*]} letters long."
    ct=0
    while [[ $ct != 14 ]]
    do
	echo "Word is: ${temp[*]}"	
	read -p "Make a guess: " guess
	n=0
	bool=0
	for i in ${s[*]}
	do
	    if [[ $guess == $i && ${temp[$n]} != $guess ]]
	    then
		temp[$n]=$guess
		bool=1
		((ct++))
	    fi
	    ((n++))
	done
	if [[ $bool == 1 ]]
	then
	    echo "Good going!"
	else
	    echo "Sorry, try again!"
	fi
    done
    echo "Congratulation! You guessed the word: sesquipedalian"
fi
