#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

#!/usr/local/bin/python3.4

import sys
import math
import glob
import string

def getWordFrequency():
    files = glob.glob("./files/*")
    dic = {}
    for f in files:
        with open(f,'r') as myFile:
            all_lines = myFile.readlines()
            for line in all_lines:
                wordList = line.split()
                for i in wordList:
                    if i not in dic:
                        dic[i] = 1
                    else:
                        dic[i] += 1
    return dic

def getDuplicates():
    files = glob.glob("./files/*")
    dic = {}
    list = []
    a = 0
    for i in files:
        a += 1
        if i not in list:
            dupList = [i]
            with open(i,'r') as myFile:
                all_lines = myFile.readlines()
                for line in all_lines:
                    wl = line.split()
            for j in files[a:]:
                with open(j,'r') as myFile2:
                    text = myFile2.readlines()
                if all_lines == text:
                    list.append(j)
                    dupList.append(j)

            for w in range(len(wl)):
                word = wl[w]
                c = word[len(word) - 1]
                if c.isalpha() == False:
                    wl[w] = word[0:-1]
            wordList = []
            for l in wl:
                if l not in wordList:
                    wordList.append(l)
            count = len(wordList)
            ct = 0
            for n in dupList:
                dupList[ct] =n[8:-4]
                ct += 1
            dic[dupList[0]] = (count, dupList)

    return dic

def price():
    file =glob.glob('./purchases/*')
    priceList = {}
    with open(file[0], 'r') as my_file:
        all_lines = my_file.readlines()[2:]
        for lines in all_lines:
            nameprice = lines.split()
            priceList[nameprice[0]] = float( nameprice[1][1:] )
    return priceList

def getPurchaseReport():
    files = glob.glob("./purchases/*")
    priceList = price()
    pReport = {}
    for i in files:
        if i != files[0]:
            with open(i,'r') as my_file:
                all_lines = my_file.readlines()[2:]
                sum = 0.0
                for lines in all_lines:
                    purList = lines.split()
                   # print(float(purList[1]))
                    sum += float(priceList[purList[0]]) * float(purList[1])
                pReport[int(i[22:-4])] = round(sum,2)
    return pReport

def getTotalSold():
    files = glob.glob("./purchases/*")
    name = {}
    with open(files[0],'r') as name_file:
        all_lines = name_file.readlines()[2:]
        for lines in all_lines:
            namelist = lines.split()
            name[namelist[0]] = 0
    for f in files:
        if f != files[0]:
            with open(f,'r') as my_file:
                all_lines = my_file.readlines()[2:]
                for lines in all_lines:
                    obj = lines.split()
                    name[obj[0]] += int(obj[1])
    return name
if __name__ == "__main__":
    print("hi")
    WordFreq_dictionary = getWordFrequency()
    for key in WordFreq_dictionary.keys():
        print(key,WordFreq_dictionary[key])
    print("============== Dup Dictionary now ============")
    #Dupe_dictionary = getDuplicates()
    #for key in Dupe_dictionary.keys():
     #   print(key," : ",Dupe_dictionary[key])

    pricelist = price()
    for key in pricelist.keys():
        print(key," : " ,pricelist[key])

    Report = getPurchaseReport()
    for key in Report.keys():
        print(key,":",Report[key])
    total = getTotalSold()
    for key in total.keys():
        print(key,":",total[key])