import glob

"""
    PERSONAL NOTES:
    files = glob.glob('./files/*') # returns a list of all files present in that directory
    dictionary = {} # create an empty dictionary
        dictionary[i] = 1   # to add an element to dictionary all we do is reference it and set value
        dictionary[i] += 1; # to update an element we simply reference it and change value
"""

def wordCounter(name): # function to be only called by getDuplicates
    sum = 0
    with open(name) as f:
            list_words = f.read().split() # list_words is a list containing all words present in the file

    # code block to remove punctuations
    for i in range(len(list_words)):
        a_word = list_words[i]
        ch = a_word[len(a_word) - 1] # ie. last character
        if ch < 'A' or ( ch > 'Z' and ch < 'a' ) or ch > 'z': # if character is not an alphabet
            list_words[i] = a_word[0:-1]

    new_list = []
    for i in list_words:
        if i not in new_list:
            new_list.append(i)

    return len(new_list)

def getDuplicates():
    dictionary = {}
    files = glob.glob("./files/*"); # files is a list of all the files in the directory ./files/
    list_completed = []
    for i in range(len(files)):
        if files[i] not in list_completed:
            list_of_dupes = [ files[i] ]
            with open(files[i]) as f:
                text = f.read()
            for j in range( i+1 , len(files) ):
                with open(files[j]) as F:
                    text2 = F.read()
                if text == text2:
                    # found a duplicate
                    list_of_dupes.append(files[j])
                    list_completed.append(files[j])

            wordCount = wordCounter(list_of_dupes[0])
            for i in range(len(list_of_dupes)): # this loop removes the ./files/ prefix in each file name
                list_of_dupes[i] = list_of_dupes[i][8:-4] # only keeping portion that has the 3 main characters in it
            dictionary[ list_of_dupes[0] ] = ( wordCount , list_of_dupes)

    return dictionary

def getWordFrequency():
    files = glob.glob('./files/*') # returns a list of all files present in that directory
    dictionary = {} # create an empty dictionary

    for a_file in files: # for each file present in directory ./file/
        with open(a_file) as f:
            list_words = f.read().split() # list_words is a list containing all words present in the file

        # code block to remove punctuations
        for i in range(len(list_words)):
            a_word = list_words[i]
            ch = a_word[len(a_word) - 1] # ie. last character
            if ch < 'A' or ( ch > 'Z' and ch < 'a' ) or ch > 'z': # if character is not an alphabet
                list_words[i] = a_word[0:-1]

        # at this point we have a list of words of a_file that do not have any punctuations in them
        # assuming punctuations may be only at the end of the file

        for i in list_words:    # iterate through each word of the list of words in a_file
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1;

    return dictionary

def getItemDict():   # used only in getPurchaseReport function
    files = glob.glob('./purchases/*') # returns a list of all files present in that directory
    itemDict = {}
    with open(files[0]) as f:
        f.readline()
        f.readline()
        name_cost = f.read().split()
    for i in range(0 , len(name_cost), 2):
        itemDict[name_cost[i]] = float( name_cost[i+1][1:] )
    # AT THIS POINT WE HAVE itemDict THAT CONTAINS ALL ITEMS AND THE COST OF EACH OF THOSE ITEMS
    return itemDict

def getPurchaseReport():
    files = glob.glob('./purchases/*') # returns a list of all files present in that directory
    itemDict = getItemDict()
    purchasereportdict = {}
    for i in files:
        if i != "./purchases/Item List.txt":
            with open(i) as f:
                f.readline()
                f.readline()
                purchase_list = f.read().split()
            cost = 0.0
            for j in range(0, len(purchase_list), 2):
                cost += float(itemDict[purchase_list[j]]) * float(purchase_list[j+1])
                # print(i, 'item count:', float(purchase_list[j+1]),' item:',purchase_list[j],'item cost',itemDict[purchase_list[j]], 'product', float(itemDict[purchase_list[j]]) * float(purchase_list[j+1]), ' cost:',cost,)
            purchasereportdict[ int(i[21:24]) ] = round(cost,2)
    return purchasereportdict

def getTotalSold():
    files = glob.glob("./purchases/*");
    with open(files[0]) as f:
        f.readline()
        f.readline()
        name_cost = f.read().split()
    cnt_dic = {}
    for i in range(0,len(name_cost),2):
        cnt_dic[name_cost[i]] = 0

    for i in files:
        if i != "./purchases/Item List.txt":
            with open(i) as f:
                f.readline()
                f.readline()
                purchase_list = f.read().split()
            for j in range(0, len(purchase_list), 2):
                cnt_dic[ purchase_list[j] ] += int(purchase_list[j+1])

    # for key in cnt_dic.keys():
    #     print(key," : ", cnt_dic[key])

    return cnt_dic

if __name__ == "__main__":
    print("hi")
    WordFreq_dictionary = getWordFrequency()
    for key in WordFreq_dictionary.keys():
        print(key,WordFreq_dictionary[key])
    print("============== Dup Dictionary now ============")
    Dupe_dictionary = getDuplicates()
    for key in Dupe_dictionary.keys():
        print(key," : ",Dupe_dictionary[key])
    print("============== Purchases here on ============")
    purchase_report_dict = getPurchaseReport()
    for key in purchase_report_dict.keys():
        print(key," : ", purchase_report_dict[key])
    print("============== Purchases part 2  ============")
    cnt_dic = getTotalSold()
    for key in cnt_dic.keys():
        print(key," : ", cnt_dic[key])